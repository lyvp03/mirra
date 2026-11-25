Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 4. Từ điển dữ liệu schema core > 4.15 inventory\_ledger — sổ kho (UC19, UC07, UC10, UC20, UC23)
### 4.15 inventory\_ledger — sổ kho (UC19, UC07, UC10, UC20, UC23)

| Cột | Kiểu | Ràng buộc | Ý nghĩa |
| --- | --- | --- | --- |
| variant\_id | uuid | FK product\_variants |  |
| delta | integer | CHECK ≠ 0 | Số thay đổi, âm là xuất |
| reason | varchar(20) | CHECK RECEIVE, ADJUST, ORDER\_PLACED, ORDER\_CANCELLED, RETURNED |  |
| order\_id | uuid | NULL, FK orders | Có khi lý do liên quan đơn |
| actor\_id | uuid | NULL, FK users | Người nhập, điều chỉnh |
| note | varchar(255) | NULL |  |

