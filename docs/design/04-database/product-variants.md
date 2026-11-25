Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 4. Từ điển dữ liệu schema core > 4.7 product\_variants — biến thể màu, size (UC05–UC07, UC17.3, UC19)
### 4.7 product\_variants — biến thể màu, size (UC05–UC07, UC17.3, UC19)

| Cột | Kiểu | Ràng buộc | Ý nghĩa |
| --- | --- | --- | --- |
| product\_id | uuid | FK products, ON DELETE CASCADE; UNIQUE (product\_id, color, size) |  |
| sku | varchar(50) | UNIQUE |  |
| color | varchar(50) |  | Tên màu hiển thị (vd Kem) |
| color\_hex | varchar(7) | NULL; CHECK color\_hex ~ '^#[0-9a-f]{6}$' | Mã màu cho swatch (UC05); cùng `color` thì cùng mã |
| size | varchar(10) |  |  |
| weight\_gram | integer | CHECK > 0 | Phụ phí cân nặng (BR11); catalog ảnh thật không có cân nặng nên seed gán mặc định theo danh mục (mục 8.3), Staff sửa được |
| stock | integer | CHECK ≥ 0 | Số lượng còn bán được; trừ khi đặt hàng, cộng lại khi hủy hoặc hoàn hàng; cảnh báo khi ≤ ngưỡng |

Không có `created_at`.

