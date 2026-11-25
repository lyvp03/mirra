Nguồn: 05-API-CONTRACT-EVENTS.md > Mirra — B5: API, contract, sự kiện > 6. Sự kiện > 6.1 SSE tới trình duyệt
### 6.1 SSE tới trình duyệt

| Endpoint | Sự kiện | Đóng khi | Kết nối lại |
| --- | --- | --- | --- |
| `POST /ai/v1/chat/conversations/{id}/messages`, `/chat/actions/{id}/confirm`, `/reject` | Mục 5.2 | `message.end`, `action.pending` hoặc `error` | Không nối lại stream cũ; web tải `GET .../messages` để lấy câu trả lời đã lưu |
| `GET /ai/v1/tryon/jobs/{id}/stream` | `job.status`, `job.completed`, `job.failed` | Job COMPLETED hoặc FAILED | Server gửi trạng thái hiện tại ngay khi nối, nên mất sự kiện giữa chừng không sao |
| `GET /api/v1/orders/{code}/payment/stream` | `payment.status` | PAID, đơn bị hủy hoặc QR hết hạn | Như trên |

Quy ước chung: mỗi 15 giây gửi một dòng chú thích `: ping` để giữ kết nối; Caddy tắt buffer cho các đường dẫn này (`flush_interval -1`); mỗi sự kiện có `event:` và `data:` dạng JSON một dòng.

