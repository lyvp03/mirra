Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 4. Từ điển dữ liệu schema core > 4.6 products — sản phẩm (UC05, UC17, UC18, UC22)
### 4.6 products — sản phẩm (UC05, UC17, UC18, UC22)

| Cột | Kiểu | Ràng buộc | Ý nghĩa |
| --- | --- | --- | --- |
| category\_id | uuid | FK categories |  |
| size\_chart\_id | uuid | NULL, FK size\_charts |  |
| name | varchar(200) |  | Tên thương mại tiếng Anh dạng `<tên riêng nữ> <loại>` (vd Lily Mini Dress); áo và quần/váy cùng set dùng chung tên riêng (Aurelia Top, Aurelia Pants) |
| name\_vi | varchar(200) | NULL | Tên mô tả tiếng Việt (vd Áo Ren Buộc Dây Tay Loe); hiển thị phụ và ghép vào nội dung tìm kiếm |
| slug | varchar(220) | UNIQUE | URL trang sản phẩm |
| description | text |  |  |
| material | varchar(200) | NULL |  |
| price | integer | NULL; CHECK > 0 | Giá gốc do Admin đặt (UC22.1) |
| status | varchar(10) | DEFAULT HIDDEN; CHECK HIDDEN, PUBLISHED; CHECK status = HIDDEN OR price IS NOT NULL | Chưa có giá thì không công khai được |
| try\_on\_enabled | boolean | DEFAULT false | UC17.4; luôn false với danh mục ACCESSORY |
| ai\_generated | boolean | DEFAULT false | Tạo từ nháp AI (UC18) |
| updated\_at | timestamptz |  | Sắp xếp, đồng bộ chỉ mục |

