Nguồn: 05-API-CONTRACT-EVENTS.md > Mirra — B5: API, contract, sự kiện > 3. Endpoint core-api > 3.2 Sản phẩm, giỏ, đơn hàng (phía khách)
### 3.2 Sản phẩm, giỏ, đơn hàng (phía khách)

| Method | Path | Quyền | UC | Chi tiết | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| GET | `/categories` | Public | UC05 |  |  |
| GET | `/products` | Public | UC05.1 |  | `q, category, color, size, price_min, price_max, in_stock`; `ids` (tối đa 30, cách nhau dấu phẩy, dùng cho tìm vector của trợ lý, B7 mục 4.5); `sort=price,-price,-created_at` |
| GET | `/products/{slug}` | Public | UC05.2 |  | Biến thể, còn hàng hay không, ảnh, bảng size, giá hiệu lực, điểm đánh giá |
| GET | `/products/{slug}/reviews` | Public | UC11 |  | Chỉ đánh giá không bị ẩn |
| GET | `/cart` | Customer | UC06 |  | Giá, tồn hiện tại kèm cảnh báo |
| PUT | `/cart/items/{variant_id}` | Customer | UC06.1, UC06.2 |  | `{quantity}`; thêm hoặc sửa |
| DELETE | `/cart/items/{variant_id}` | Customer | UC06.2 |  |  |
| POST | `/cart/merge` | Customer | UC06.3 |  | `{lines: [{variant_id, quantity}]}` từ giỏ trình duyệt |
| POST | `/checkout/quote` | Public | UC07.1, UC07.2 | ✓ | Kiểm tồn, giá, tính phí ship |
| POST | `/orders` | Public | UC07 | ✓ | `Idempotency-Key`; Customer gửi kèm token, Guest gửi email |
| GET | `/orders` | Customer | UC09 |  | Đơn của mình |
| GET | `/orders/{code}` | Owner | UC09 |  | Kèm lịch sử trạng thái, thanh toán |
| POST | `/orders/{code}/cancel` | Owner | UC10 |  | Chỉ khi chưa xác nhận |
| POST | `/orders/{code}/reviews` | Owner (Customer) | UC11 |  | `{variant_id, rating, content}`; đơn đã giao |
| GET | `/orders/{code}/payment` | Owner | UC08 | ✓ | QR, số tiền, trạng thái, hạn |
| GET | `/orders/{code}/payment/stream` | Owner | UC08 | ✓ | SSE báo đã thanh toán |
| POST | `/payments/payos/webhook` | payOS | UC08 | ✓ |  |

