Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 4. Từ điển dữ liệu schema core > 4.1 users — tài khoản Customer, Staff, Admin (UC01–UC04, UC24, UC25)
### 4.1 users — tài khoản Customer, Staff, Admin (UC01–UC04, UC24, UC25)

| Cột | Kiểu | Ràng buộc | Ý nghĩa |
| --- | --- | --- | --- |
| email | varchar(255) | UNIQUE | Lưu chữ thường |
| password\_hash | varchar(255) | NULL | Argon2id; rỗng khi Staff còn trạng thái INVITED |
| full\_name | varchar(100) |  |  |
| phone | varchar(15) | NULL |  |
| role | varchar(10) | CHECK CUSTOMER, STAFF, ADMIN | Guest không có bản ghi |
| status | varchar(10) | DEFAULT ACTIVE; CHECK ACTIVE, LOCKED, INVITED | LOCKED do Admin khóa (UC24.2) |
| locked\_reason | varchar(255) | NULL | Lý do khóa |
| email\_verified\_at | timestamptz | NULL | Rỗng = chưa xác thực, không được thử đồ (BR19) |

Khóa tạm 15 phút sau 5 lần đăng nhập sai dùng bộ đếm có hạn trong Redis, không lưu trong bảng.

