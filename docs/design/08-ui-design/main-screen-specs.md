Nguồn: 08-UI-DESIGN.md > B8 – Thiết kế giao diện > Đặc tả màn hình chính
## Đặc tả màn hình chính

Đặc tả các màn trọng tâm: thành phần chính, thao tác và trạng thái. Các màn còn lại xem trực tiếp trên canvas mockup.

**S01 — Trang chủ**

| Mục | Nội dung |
| --- | --- |
| Thành phần | Thanh khuyến mãi, header, hero slider, “u đãi nổi bật” (6 cột), “Mới”, dòng sản phẩm theo tab, 2 banner lookbook, “Bán chạy”, khối Mirra AI, footer, nút chat nổi |
| Thao tác | Vào danh mục, mở sản phẩm, chuyển tab dòng sản phẩm, mở chat |
| Trạng thái | Mặc định; số giỏ hiện khi có hàng |

**S02 — Danh sách sản phẩm**

| Mục | Nội dung |
| --- | --- |
| Thành phần | Breadcrumb, tiêu đề + tagline, băng danh mục con, chip lọc, chọn số cột, sắp xếp, lưới 6 cột, chip lọc đang áp dụng, nút xem thêm, đoạn SEO |
| Thao tác | Lọc (mở S02b), sắp xếp, đổi số cột, xem thêm, mở sản phẩm |
| Trạng thái | Có lọc / không; đang tải (skeleton); không có kết quả |

**S04 — Chi tiết sản phẩm**

| Mục | Nội dung |
| --- | --- |
| Thành phần | Gallery ảnh dọc; cột phải dính: breadcrumb, tên, đánh giá, giá, swatch màu, ô size, số lượng, 2 nút (Thêm giỏ / Mua ngay), khối Thử đồ AI, 4 cam kết, accordion; khối “Mirra phối cùng”; đánh giá; “Có thể bạn sẽ thích” |
| Thao tác | Chọn màu/size, đổi số lượng, thêm giỏ, mua ngay, mở bảng size (S04b), Thử đồ AI / webcam, hỏi Mirra |
| Trạng thái | Size hết hàng (gạch, khóa); dòng sắp hết khi tồn ≤ 3; nút thử đồ: khách chưa đăng nhập → dẫn đăng nhập, chưa xác thực email → khóa kèm lý do |

**S06 — Giỏ hàng**

| Mục | Nội dung |
| --- | --- |
| Thành phần | Thanh “Chọn tất cả”, danh sách món (checkbox, ảnh, biến thể đổi tại chỗ, số lượng, xóa), tóm tắt dính bên phải, gợi ý Mirra |
| Thao tác | Chọn món thanh toán, đổi số lượng/biến thể, xóa, sang checkout |
| Trạng thái | Giỏ trống; món vượt tồn (cảnh báo + chặn); freeship đạt/chưa đạt |

**S07 — Checkout**

| Mục | Nội dung |
| --- | --- |
| Thành phần | Email, thông tin giao hàng (Tỉnh → Phường/Xã → địa chỉ), vận chuyển, thanh toán (VietQR/COD), ghi chú, tóm tắt dính |
| Thao tác | Điền form, chọn vận chuyển/thanh toán, đặt hàng |
| Trạng thái | Lỗi từng trường (vd sĐT); phí ship “—” trước khi chọn địa chỉ |

**S08 — Thanh toán VietQR**

| Mục | Nội dung |
| --- | --- |
| Thành phần | Mã QR, số tiền, nội dung chuyển (= mã đơn), thông tin tài khoản, đếm ngược 15 phút |
| Thao tác | Quét/sao chép, đổi sang COD, hủy đơn |
| Trạng thái | Chờ thanh toán (đếm ngược); đã thanh toán → sang S09; hết hạn → đơn tự hủy, hoàn tồn kho |

**S24 — Chat Mirra AI**

| Mục | Nội dung |
| --- | --- |
| Thành phần | Header (avatar, “trả lời bằng AI”), bong bóng AI/khách, ProductsCard, OutfitCard, ConfirmCard, chip gợi ý, ô nhập |
| Thao tác | Nhắn, bấm chip, xem/thử sản phẩm, thêm cả set, xác nhận thao tác ghi |
| Trạng thái | Đang trả lời (typing); thẻ xác nhận hết hạn sau 10 phút; hết lượt (Guest 20/phiên, Customer 50/ngày) → khóa ô nhập |

**S21 — Thử đồ bằng ảnh**

| Mục | Nội dung |
| --- | --- |
| Thành phần | 3 bước (chọn ảnh → đang thử → kết quả), hạn mức còn lại, ô tải ảnh, ảnh sản phẩm, khung kết quả, nút sau kết quả (thêm giỏ, tạo video, lưu, thử ảnh khác) |
| Thao tác | Tải ảnh, chạy thử, tạo video 3–5s, lưu lịch sử |
| Trạng thái | Modal đồng ý (S20) lần đầu; ảnh không đạt (báo lý do); đang xử lý (SSE); hết lượt (khóa nút) |

