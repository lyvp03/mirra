Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 8. Index, quy tắc xóa, dữ liệu seed > 8.3 Dữ liệu seed
### 8.3 Dữ liệu seed

| Dữ liệu | Bảng | Nguồn |
| --- | --- | --- |
| Tỉnh/thành, phường/xã và tọa độ tâm | `provinces`, `wards` | Danh mục hành chính chính thức + tọa độ tâm |
| Danh mục và vị trí mặc | `categories` | 10 danh mục: TOP (áo sơ mi & áo kiểu, áo thun & croptop, áo len & cardigan), BOTTOM (quần, chân váy), ONE\_PIECE (đầm & váy liền, jumpsuit), OTHER (áo khoác), ACCESSORY (giày dép, túi xách) |
| Bảng size | `size_charts` | 3 bảng: `nu_ao_dam`, `nu_quan_chan_vay` (S–XL), `nu_giay` (35–39 theo chiều dài bàn chân); túi Freesize, không gắn bảng size |
| Sản phẩm, biến thể, ảnh, khuyến mãi | `products`, `product_variants`, `product_images`, `promotions` | Catalog từ ảnh thật (`mirra-data.zip`, 24/11): 193 sản phẩm, 1008 SKU, 339 ảnh WebP 720×900 nạp lên bucket `products`; `color_hex` lấy từ catalog; `weight_gram` mặc định theo danh mục (gram): áo sơ mi & áo kiểu 200, áo thun & croptop 180, áo len & cardigan 350, quần 400, chân váy 300, đầm & váy liền 350, jumpsuit 450, áo khoác 600, giày dép 700, túi xách 500. `price` = `compare_at_price_vnd` nếu có, không thì `price_vnd`; sản phẩm có `compare_at_price_vnd` thêm một dòng `promotions` với `sale_price` = `price_vnd` |
| Cấu hình mặc định | `settings` + dòng đầu của `setting_history` | Giá trị đã chốt ở B1 mục 6.2 và 6.3: hạn mức thử đồ, hạn mức chat, ngưỡng tồn thấp, bậc phí ship và ngưỡng miễn phí, thời lượng/số phiên/trần ngân sách webcam, số ngày giữ ảnh, cờ bật tắt tính năng |
| Tài khoản Admin đầu tiên | `users` | Biến môi trường lúc triển khai |

Seed chạy lại không tạo trùng (B3 mục 5.3). Tên khóa cấu hình và schema giá trị của từng khóa chốt ở B5 cùng API cấu hình.
