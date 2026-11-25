Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 4. Từ điển dữ liệu schema core > 4.9 promotions — giá khuyến mãi (UC22.2)
### 4.9 promotions — giá khuyến mãi (UC22.2)

| Cột | Kiểu | Ràng buộc | Ý nghĩa |
| --- | --- | --- | --- |
| product\_id | uuid | FK products, ON DELETE CASCADE |  |
| sale\_price | integer | CHECK > 0 | Nhỏ hơn giá gốc, kiểm tra ở ứng dụng |
| starts\_at, ends\_at | timestamptz | CHECK starts\_at < ends\_at | Không chồng lấn theo sản phẩm, kiểm tra ở ứng dụng |

