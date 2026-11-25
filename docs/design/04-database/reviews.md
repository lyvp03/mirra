Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 4. Từ điển dữ liệu schema core > 4.16 reviews — đánh giá (UC11)
### 4.16 reviews — đánh giá (UC11)

| Cột | Kiểu | Ràng buộc | Ý nghĩa |
| --- | --- | --- | --- |
| order\_id, variant\_id | uuid | PK; FK order\_items (order\_id, variant\_id) ON DELETE CASCADE | Mỗi dòng đơn một đánh giá; người viết lấy từ đơn |
| rating | smallint | CHECK 1–5 |  |
| content | text | NULL |  |
| hidden | boolean | DEFAULT false | Staff ẩn |

