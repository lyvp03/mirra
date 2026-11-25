Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 5. Từ điển dữ liệu schema ai > 5.8 pending\_actions — hành động chờ xác nhận (UC16)
### 5.8 pending\_actions — hành động chờ xác nhận (UC16)

| Cột | Kiểu | Ràng buộc | Ý nghĩa |
| --- | --- | --- | --- |
| conversation\_id | uuid | FK conversations, ON DELETE CASCADE |  |
| tool\_name | varchar(50) |  |  |
| args | jsonb |  | Tham số tool hiển thị trên thẻ xác nhận và gửi lại nguyên khối khi xác nhận |
| status | varchar(10) | CHECK PENDING, CONFIRMED, REJECTED, EXPIRED |  |
| expires\_at | timestamptz |  |  |
| decided\_at | timestamptz | NULL |  |

