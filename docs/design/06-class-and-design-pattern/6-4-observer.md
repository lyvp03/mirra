Nguồn: 06-CLASS-AND-DESIGN-PATTERN.md > Mirra — B6: Thiết kế lớp và design pattern > 6. Design pattern > 6.4 Observer
### 6.4 Observer

Ba mức, cùng ý: bên phát không phụ thuộc bên nhận.

| Mức | Bên phát | Bên nhận |
| --- | --- | --- |
| Trong một request | Service đăng callback vào `UnitOfWork.after_commit` | Callback chạy khi commit thành công (phát sự kiện, xếp job, báo SSE) |
| Giữa service | `EventPublisher` ghi Redis Streams | `IndexSyncConsumer`, `EmailConsumer`, `TryOnJobConsumer`, bộ đệm cấu hình của ai |
| Tới trình duyệt | `Notifier` (pub/sub) | Handler SSE của thanh toán và job |

