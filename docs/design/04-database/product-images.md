Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 4. Từ điển dữ liệu schema core > 4.8 product\_images — ảnh sản phẩm (UC05, UC17.3, UC12)
### 4.8 product\_images — ảnh sản phẩm (UC05, UC17.3, UC12)

| Cột | Kiểu | Ràng buộc | Ý nghĩa |
| --- | --- | --- | --- |
| product\_id | uuid | FK products, ON DELETE CASCADE |  |
| color | varchar(50) | NULL | Rỗng = ảnh chung mọi màu |
| kind | varchar(10) | CHECK MODEL, FLAT\_LAY | MODEL: ảnh người mẫu mặc đồ (ảnh chính của catalog); FLAT\_LAY: ảnh trải phẳng, tùy chọn. Ảnh tham chiếu thử đồ của một màu là ảnh FLAT\_LAY nếu có, không thì ảnh MODEL có `position` nhỏ nhất |
| object\_key | varchar(255) |  | Khóa trong bucket `products` |
| position | smallint | DEFAULT 0 | Thứ tự hiển thị trong cùng màu; 0 là ảnh chính diện, làm ảnh đại diện |

Ảnh sản phẩm tỉ lệ 4:5 (WebP 720×900, giữ nguyên ảnh gốc). Nhiều góc chụp của cùng mẫu, cùng màu là nhiều dòng theo `position`; góc chụp không lưu cột riêng. Một ảnh người mẫu mặc set (áo + quần/váy cùng chất) dùng cho cả 2 sản phẩm: mỗi sản phẩm một dòng, cùng `object_key`.

