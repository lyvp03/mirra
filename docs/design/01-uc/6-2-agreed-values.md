Nguồn: 01-UC.md > Mirra — B1: Phân rã và đặc tả use case > 6. Giả định cần kiểm chứng và giá trị đã chốt > 6.2 Giá trị đã chốt
### 6.2 Giá trị đã chốt

| Giá trị | Giá trị | Dùng ở |
| --- | --- | --- |
| Thời hạn access token / refresh token | 15 phút / 7 ngày | UC02 |
| Tạm khóa đăng nhập | Sai 5 lần trong 15 phút → khóa 15 phút | UC02 |
| Độ dài mật khẩu tối thiểu | 8 ký tự | UC01, UC04.1 |
| Hạn link xác thực email / link đặt lại mật khẩu | 24 giờ / 30 phút | UC01.1, UC03 |
| Số địa chỉ tối đa | 5 | UC04.2 |
| Dung lượng ảnh tối đa | 5 MB, JPG/PNG/WebP | UC12.2, UC17.3 |
| Số set mỗi lần gợi ý | 1–3 | UC31 |
| Hạn mức chat | Guest 20 tin/phiên; Customer 50 tin/ngày; Staff và Admin 200 tin/ngày | UC15, UC27 |
| Phí giao hàng | Tính theo khoảng cách từ kho tới địa chỉ nhận, xem mục 6.3 | UC07.2, UC27 |
| Ngưỡng cảnh báo hàng sắp hết | Tồn ≤ 3 mỗi SKU; Admin đổi được toàn cục | UC19.1, UC27 |

Lý do chọn hai mức:

- **Hạn mức chat:** 50 tin/ngày đủ cho một khách hỏi, phối đồ và đổi set nhiều lần, nhưng chặn được script spam làm tốn chi phí LLM; nhân viên dùng trợ lý làm việc cả ngày nên để cao hơn.
- **Ngưỡng hàng sắp hết:** shop nhỏ, mỗi SKU thường chỉ vài đến vài chục chiếc; còn 3 chiếc là lúc cần nhập thêm.

