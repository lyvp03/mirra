Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 5. Từ điển dữ liệu schema ai > 5.10 search\_documents — chỉ mục tìm kiếm ngữ nghĩa (UC15, UC31)
### 5.10 search\_documents — chỉ mục tìm kiếm ngữ nghĩa (UC15, UC31)

| Cột | Kiểu | Ràng buộc | Ý nghĩa |
| --- | --- | --- | --- |
| source\_type | varchar(10) | PK; CHECK PRODUCT, FAQ |  |
| source\_id | uuid | PK, ref products hoặc faqs |  |
| content | text |  | Văn bản đã ghép để tạo embedding, trả cho agent; với sản phẩm gồm `name`, `name_vi`, danh mục, chất liệu, mô tả, màu |
| embedding | vector(d) |  | d theo model embedding chọn sau benchmark |
| visible | boolean |  | Sản phẩm PUBLISHED hoặc FAQ active |
| updated\_at | timestamptz |  | Thời điểm đồng bộ gần nhất |

Giá, tồn kho không chép sang đây; agent lấy trực tiếp từ core khi trả lời. Không có `id`, `created_at`.

