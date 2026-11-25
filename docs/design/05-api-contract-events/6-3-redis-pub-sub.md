Nguồn: 05-API-CONTRACT-EVENTS.md > Mirra — B5: API, contract, sự kiện > 6. Sự kiện > 6.3 Redis pub/sub
### 6.3 Redis pub/sub

| Kênh | Bên phát | Bên nghe | Nội dung |
| --- | --- | --- | --- |
| `mirra:job:{job_id}` | ai-worker, ai-service (webhook) | Handler SSE của ai-service | `{status, error_code?}` |
| `mirra:payment:{order_code}` | core-api (webhook, hủy đơn) | Handler SSE của core-api | `{status, order_status}` |

Pub/sub không lưu tin; handler SSE đọc trạng thái từ DB khi mở kết nối nên mất một tin không làm kẹt màn hình.

