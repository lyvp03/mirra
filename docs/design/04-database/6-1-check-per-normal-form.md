Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 6. Kiểm tra 3NF và ngoại lệ có chủ đích > 6.1 Kiểm tra theo từng dạng chuẩn
### 6.1 Kiểm tra theo từng dạng chuẩn

| Dạng chuẩn | Điều kiện | Cách đáp ứng |
| --- | --- | --- |
| 1NF | Mọi cột nguyên tố, không có nhóm lặp | Nhóm lặp tách thành bảng: món trong giỏ (`cart_items`), dòng đơn (`order_items`), món trong job thử đồ (`tryon_job_items`). Cột JSONB là ngoại lệ ở 6.2, được xử lý như một giá trị nguyên khối |
| 2NF | Cột không khóa phụ thuộc toàn bộ khóa ghép | `cart_items.quantity`, `reviews.rating/content/hidden`, `search_documents.content/embedding` phụ thuộc cả hai thành phần khóa. Ở `order_items`, tên, màu, size, giá là giá trị tại thời điểm của chính đơn đó, nên phụ thuộc cả (order\_id, variant\_id) chứ không chỉ variant\_id |
| 3NF | Không có phụ thuộc bắc cầu qua cột không khóa | Tên tỉnh tách sang `provinces` (ward → province\_code → tên tỉnh); vị trí mặc nằm ở `categories.slot`, không lặp ở sản phẩm; người viết đánh giá lấy từ đơn, không lưu `user_id` ở `reviews`; tổng tiền đơn, số dư sổ kho, trạng thái trước đó của đơn, hạn xóa ảnh, số tin trong hội thoại, ngân sách webcam đều tính khi cần, không lưu |

