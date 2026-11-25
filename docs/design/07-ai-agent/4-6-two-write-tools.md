Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 4. Tool > 4.6 Hai tool ghi
### 4.6 Hai tool ghi

**`add_to_cart`** (BR05, BR17):

- Thẻ xác nhận: "Thêm *{tên}*, màu {màu}, size {size}, số lượng {n} vào giỏ".
- Khi được duyệt: đổi slug + màu + size thành `variant_id`, đọc số lượng đang có trong giỏ, rồi `PUT /cart/items/{variant_id}` với tổng mới. `PUT` của B5 là đặt số lượng, không phải cộng thêm, nên phải đọc trước.
- Tổng vượt 10 (BR05), hết hàng hoặc không có biến thể thì core báo lỗi, agent giải thích.
- System prompt dặn agent gọi `get_product` trước để chắc màu và size còn hàng, tránh khách bấm xác nhận rồi mới biết hết.

**`update_order_status`** (BR08, BR13, BR17):

- `action` thuộc `confirm`, `ship`, `deliver`, `delivery_failed`, `return`, `cancel`, khớp các endpoint `/admin/orders/{id}/...` của B5. Tool tìm `id` từ `order_code`.
- `ship` cần `tracking_no`; `cancel` và `delivery_failed` cần `reason`; xác nhận đơn COD của Guest cần `phone_checked = true` (BR13). Thiếu thì schema báo lỗi ngay, agent hỏi lại Staff trước khi tạo thẻ xác nhận.
- Thẻ xác nhận: "Chuyển đơn {mã} sang {trạng thái}" kèm mã vận đơn hoặc lý do nếu có.
- Ai được chuyển trạng thái nào vẫn do `OrderStateMachine` của core quyết, vd chỉ Admin hủy đơn đang giao (UC23.1). Tool không tự kiểm lại luật này, chỉ chuyển lỗi `INVALID_TRANSITION` của core thành `ToolMessage`.

