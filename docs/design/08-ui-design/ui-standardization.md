Nguồn: 08-UI-DESIGN.md > B8 – Thiết kế giao diện > Chuẩn hóa giao diện
## Chuẩn hóa giao diện

Mọi giá trị dưới đây lấy từ Design System Mirra (token) để mọi màn dùng thống nhất.

**Màu sắc**

| Vai trò | Mã | Dùng cho |
| --- | --- | --- |
| Nền | #FFFFFF | Nền trang, header, drawer, thẻ |
| Nền phụ | #F6F6F6 | Panel tóm tắt đơn, header bảng admin |
| Nền ảnh | #EFEDEE | Nền sau ảnh sản phẩm 4:5 |
| Chữ chính | #111111 | Chữ, icon, nút chính |
| Chữ phụ | #66646A | Chữ phụ, breadcrumb, meta |
| Nhấn lilac | #D7A5DA | Thanh khuyến mãi, fill của Mirra AI |
| Lilac nhạt | #F4E6F5 | Nền nội dung do AI tạo |
| Lilac đậm | #7D3D82 | Chữ/icon AI |
| Rượu (logo) | #840725 | Logo Mirra, viền focus, link |
| Sale | #B3261E | Giá sale, mục Sale |
| Badge | #0B1324 | Nền nhãn sản phẩm |

Màu trạng thái: success #1B6B3A, warning #8A4B00, info #1F4FA8, danger #B3261E — chỉ dùng cho nhãn trạng thái, băng thông báo và dòng tồn kho, kèm chữ, không dùng trang trí.

**Kiểu chữ**

Một họ chữ Plus Jakarta Sans cho toàn bộ (miễn phí, hỗ trợ tiếng Việt); riêng logo “Mirra” dùng Dancing Script. Tiêu đề đậm 500, không dùng bold.

| Kiểu | Cỡ / giãn dòng | Dùng cho |
| --- | --- | --- |
| Hero | 48 / 54 (mobile 32/38) | Tiêu đề banner |
| Tiêu đề trang | 28 / 36 (mobile 24/32) | H1 các trang |
| Tiêu đề mục | 24 / 32 | Mục trang chủ, PDP |
| Tên sản phẩm (PDP) | 24 / 32 | Trang chi tiết |
| Body | 16 / 24 | Chữ thường, form, chat |
| Nhỏ | 14 / 20 | Tên trên thẻ, bảng, meta |
| Caption | 12 / 16 | Nhãn thương hiệu, breadcrumb |
| Micro | 11 / 14 | Badge, thanh khuyến mãi |

**Bo góc:** mặc định 0px (nút, input, thẻ, drawer — Mirra vuông); badge/chip 4px; bong bóng và thẻ chat 16px (hình bo duy nhất, đánh dấu Mirra AI); swatch và nút chat nổi bo tròn.

**Lưới & khoảng cách:** container tối đa 1440px; lề hai bên 36px (desktop), 16px (mobile). Lưới sản phẩm: 6 cột trang danh sách (chuyển được 4), 4 cột trang chủ, 2 cột mobile; cách cột 8px, cách hàng 24px. Các mục trang chủ cách nhau 64px (mobile 48px).

**Thiết bị & độ phân giải:** thiết kế responsive, mốc chuyển 768px. Cửa hàng (Guest/Customer) chạy cả desktop (khung 1440px) và mobile (khung 390px). Khu Staff/Admin chỉ desktop. Ảnh sản phẩm luôn tỉ lệ 4:5 (token `image-ratio` = 4/5; ảnh gốc 720×900, không cắt).

