Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 4. Từ điển dữ liệu schema core > 4.10 cart\_items — giỏ hàng của người đã đăng nhập (UC06)
### 4.10 cart\_items — giỏ hàng của người đã đăng nhập (UC06)

| Cột | Kiểu | Ràng buộc | Ý nghĩa |
| --- | --- | --- | --- |
| user\_id | uuid | PK, FK users, ON DELETE CASCADE |  |
| variant\_id | uuid | PK, FK product\_variants, ON DELETE CASCADE |  |
| quantity | smallint | CHECK 1–10 |  |

Giỏ của Guest nằm ở trình duyệt. Không có `id`, `created_at`.

