Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 4. Từ điển dữ liệu schema core > 4.12 order\_items — dòng đơn (UC07, UC09, UC11)
### 4.12 order\_items — dòng đơn (UC07, UC09, UC11)

| Cột | Kiểu | Ràng buộc | Ý nghĩa |
| --- | --- | --- | --- |
| order\_id | uuid | PK, FK orders, ON DELETE CASCADE |  |
| variant\_id | uuid | PK, FK product\_variants |  |
| product\_name | varchar(200) |  | Tên lúc mua |
| color, size | varchar(50), varchar(10) |  | Biến thể lúc mua |
| unit\_price | integer | CHECK > 0 | Giá hiệu lực lúc đặt, đã tính khuyến mãi |
| quantity | smallint | CHECK 1–10 |  |

