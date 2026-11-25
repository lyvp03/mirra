Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 4. Từ điển dữ liệu schema core > 4.2 auth\_tokens — refresh token và token dùng một lần (UC01–UC03, UC25)
### 4.2 auth\_tokens — refresh token và token dùng một lần (UC01–UC03, UC25)

| Cột | Kiểu | Ràng buộc | Ý nghĩa |
| --- | --- | --- | --- |
| user\_id | uuid | FK users, ON DELETE CASCADE |  |
| kind | varchar(20) | CHECK REFRESH, VERIFY\_EMAIL, RESET\_PASSWORD, SET\_PASSWORD |  |
| token\_hash | char(64) | UNIQUE | SHA-256 của token; token gốc chỉ gửi cho người dùng |
| expires\_at | timestamptz |  | 7 ngày, 24 giờ, 30 phút, 24 giờ theo loại |
| used\_at | timestamptz | NULL | Đã dùng hoặc bị thu hồi |

Access token là JWT, không lưu. Bảng không có `created_at`.

