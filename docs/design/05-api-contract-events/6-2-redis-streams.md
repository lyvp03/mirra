Nguồn: 05-API-CONTRACT-EVENTS.md > Mirra — B5: API, contract, sự kiện > 6. Sự kiện > 6.2 Redis Streams
### 6.2 Redis Streams

Mọi thông điệp có hai trường Redis: `type` và `data` (chuỗi JSON). `data` luôn có `event_id` (UUID), `occurred_at`, `version` (bắt đầu từ 1) cùng các trường riêng dưới đây.

| Stream | `type` | Trường riêng | Bên ghi | Consumer group → bên đọc |
| --- | --- | --- | --- | --- |
| `mirra:events:catalog` | `product.changed` | `product_id`, `change`: CREATED, UPDATED, VISIBILITY, DELETED | core-api, sau commit | `ai-index` → ai-worker (`IndexSyncConsumer`) |
| `mirra:events:catalog` | `faq.changed` | `faq_id`, `change`: CREATED, UPDATED, DELETED | core-api | `ai-index` → ai-worker |
| `mirra:events:settings` | `settings.updated` | `key` | core-api | `ai-service`, `ai-worker` (mỗi service một group để cùng nhận) |
| `mirra:jobs:email` | `email.send` | `template`, `to`, `params` | core-api | `core-worker` → `EmailConsumer` |
| `mirra:jobs:tryon` | `tryon.run` | `job_id` | ai-service | `ai-worker` → `TryOnJobRunner` |

Mẫu email (`template`): `VERIFY_EMAIL`, `RESET_PASSWORD`, `STAFF_INVITE`, `ORDER_PLACED`, `ORDER_STATUS_CHANGED`, `ORDER_CANCELLED`, `LATE_PAYMENT`, `REFUNDED`. Nội dung email do core-worker dựng từ template Jinja2.

Sự kiện chỉ mang ID; bên đọc lấy dữ liệu mới nhất qua `/internal/v1` hoặc DB của mình, nên thứ tự đến không làm sai kết quả.

Xử lý tin cậy:

- Giao ít nhất một lần: bên đọc `XACK` sau khi xử lý xong, xử lý phải idempotent (upsert SearchDocument; job try-on bỏ qua nếu đã không còn PENDING).
- Tin treo quá 5 phút được lấy lại bằng `XAUTOCLAIM`; giao quá 5 lần thì chuyển sang `mirra:dead` và ghi log lỗi.
- Mỗi stream giới hạn khoảng 10.000 tin (`XADD MAXLEN ~`).
- Core phát sự kiện sau commit; nếu Redis lỗi đúng lúc đó thì sự kiện mất. Chấp nhận với phạm vi đồ án và bù bằng lệnh `reindex` của ai-worker (dựng lại toàn bộ SearchDocument).

