Nguồn: 05-API-CONTRACT-EVENTS.md > Mirra — B5: API, contract, sự kiện > 2. Xác thực và phân quyền > 2.3 Guest
### 2.3 Guest

| Trường hợp | Cách nhận diện |
| --- | --- |
| Đặt hàng, tra đơn, hủy đơn | `POST /orders` trả `order_token` một lần (core lưu hash vào `orders.guest_token_hash`), email gửi link `/orders/{code}?token=...`. Web gửi lại bằng header `X-Order-Token`. Token hết hạn sau `order.guest_link_days` ngày (mặc định 7) kể từ khi đơn vào trạng thái cuối (DELIVERED, CANCELLED, RETURNED); quá hạn trả `ORDER_TOKEN_EXPIRED` (BR12). |
| Chat | `POST /ai/v1/chat/guest-sessions` cấp `guest_session_id` ngẫu nhiên (ai-service lưu trong Redis 24 giờ kèm bộ đếm tin). Web gửi lại bằng header `X-Guest-Session`; có thêm giới hạn theo IP để không lách hạn mức bằng cách xin phiên mới |
| Giỏ hàng | Ở trình duyệt; gộp vào server qua `POST /cart/merge` sau khi đăng nhập |

