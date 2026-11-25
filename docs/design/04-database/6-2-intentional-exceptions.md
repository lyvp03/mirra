Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 6. Kiểm tra 3NF và ngoại lệ có chủ đích > 6.2 Ngoại lệ có chủ đích
### 6.2 Ngoại lệ có chủ đích

| Chỗ | Vì sao vẫn lưu | Cách giữ đúng |
| --- | --- | --- |
| `product_variants.stock` (tính được từ tổng `inventory_ledger.delta`) | Kiểm tra và trừ tồn phải nằm trong một câu `UPDATE ... WHERE stock >= :qty` có khóa dòng để không bán quá số lượng; cộng sổ kho mỗi lần đặt hàng thì chậm và dễ tranh chấp | Mọi thay đổi tồn đi qua `StockPolicy`, ghi `inventory_ledger` trong cùng transaction |
| `order_items.product_name, color, size, unit_price`; địa chỉ nhận trong `orders` | Là sự thật tại lúc đặt; sản phẩm, giá, sổ địa chỉ đổi về sau không được làm đổi đơn cũ | Ghi một lần khi tạo đơn, không sửa |
| `payments.amount` | Số tiền đã gửi cho cổng thanh toán, dùng đối chiếu webhook | Ghi khi tạo đơn bằng tổng dòng đơn + phí ship; đơn không sửa dòng sau khi tạo |
| `webcam_sessions.max_seconds` | Giá trị cấu hình lúc mở phiên; Admin đổi cấu hình không được làm sai phiên đang chạy | Ghi khi tạo phiên |
| `search_documents.content, embedding` (dẫn xuất từ `products`, `faqs` của core) | Bản đọc phục vụ tìm kiếm ở service khác; embedding đắt, không tính lại mỗi truy vấn | Cập nhật khi nhận sự kiện từ core; chấp nhận trễ vài giây |
| JSONB `size_charts.measurements` | Bảng số đo hiển thị nguyên khối, số cột khác nhau theo loại đồ | Seed, không truy vấn theo số đo |
| JSONB `settings.value`, `setting_history.new_value` | Mỗi khóa có kiểu giá trị riêng (số, bảng bậc phí ship, cờ) | Kiểm tra theo schema của từng khóa ở `SettingsService` trước khi ghi |
| JSONB `pending_actions.args` | Tham số khác nhau theo từng tool, chỉ hiển thị và gửi lại nguyên khối | Kiểm tra bằng schema của tool lúc tạo và lúc thực thi |
| JSONB `outfit_suggestions.sets`, `webcam_sessions.target`, `chat_messages.cards` | Bản chụp nội dung đã hiển thị cho khách; không lọc hay nối theo món bên trong | Giá, tồn hiện tại luôn lấy lại từ core khi hiển thị |

