Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 4. Từ điển dữ liệu schema core > 4.13 order\_status\_history — lịch sử trạng thái đơn (UC09, UC10, UC20, UC23, UC29)
### 4.13 order\_status\_history — lịch sử trạng thái đơn (UC09, UC10, UC20, UC23, UC29)

| Cột | Kiểu | Ràng buộc | Ý nghĩa |
| --- | --- | --- | --- |
| order\_id | uuid | FK orders, ON DELETE CASCADE |  |
| status | varchar(25) | CHECK như orders.status | Trạng thái mới; trạng thái cũ là dòng liền trước |
| actor\_id | uuid | NULL, FK users | Rỗng = hệ thống hoặc Guest |
| note | varchar(255) | NULL | Lý do hủy, giao thất bại… |

