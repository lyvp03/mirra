Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 4. Từ điển dữ liệu schema core > 4.4 addresses — sổ địa chỉ (UC04)
### 4.4 addresses — sổ địa chỉ (UC04)

| Cột | Kiểu | Ràng buộc | Ý nghĩa |
| --- | --- | --- | --- |
| user\_id | uuid | FK users, ON DELETE CASCADE | Tối đa 5 địa chỉ, kiểm tra ở ứng dụng |
| receiver\_name | varchar(100) |  |  |
| phone | varchar(15) |  |  |
| ward\_code | varchar(10) | FK wards |  |
| street | varchar(255) |  | Số nhà, đường |
| is\_default | boolean | DEFAULT false; UNIQUE (user\_id) WHERE is\_default | Mỗi người một địa chỉ mặc định |

