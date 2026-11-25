Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 4. Từ điển dữ liệu schema core > 4.14 payments — thanh toán (UC07, UC08, UC20.3, UC23.2)
### 4.14 payments — thanh toán (UC07, UC08, UC20.3, UC23.2)

| Cột | Kiểu | Ràng buộc | Ý nghĩa |
| --- | --- | --- | --- |
| order\_id | uuid | UNIQUE, FK orders | Mỗi đơn một thanh toán |
| method | varchar(10) | CHECK COD, VIETQR |  |
| status | varchar(20) | CHECK UNPAID, PAID, REFUND\_REQUIRED, REFUNDED |  |
| amount | integer | CHECK > 0 | Số tiền phải thu, đối chiếu với cổng thanh toán |
| gateway\_ref | varchar(100) | NULL | Mã yêu cầu thanh toán bên payOS |
| txn\_id | varchar(100) | NULL, UNIQUE | Mã giao dịch; chặn xử lý webhook trùng |
| paid\_at | timestamptz | NULL |  |
| refund\_txn\_ref | varchar(100) | NULL | UC23.2 |
| refunded\_at | timestamptz | NULL |  |

Không có `created_at` (tạo cùng đơn).

