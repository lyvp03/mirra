Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 4. Từ điển dữ liệu schema core > 4.5 categories, size\_charts — danh mục và bảng size (seed)
### 4.5 categories, size\_charts — danh mục và bảng size (seed)

| Bảng.cột | Kiểu | Ràng buộc | Ý nghĩa |
| --- | --- | --- | --- |
| categories.name | varchar(100) |  |  |
| categories.slug | varchar(120) | UNIQUE |  |
| categories.slot | varchar(10) | CHECK TOP, BOTTOM, ONE\_PIECE, OTHER, ACCESSORY | Vị trí mặc; dùng kiểm tra set 1 trên + 1 dưới, không nhận đầm liền (BR20); ACCESSORY (giày, túi) không vào set, không bật thử đồ |
| size\_charts.name | varchar(100) |  |  |
| size\_charts.measurements | jsonb |  | Bảng số đo theo size, hiển thị nguyên khối |

