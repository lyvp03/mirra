Nguồn: 01-UC.md > Mirra — B1: Phân rã và đặc tả use case > 1. Quy ước và thay đổi so với SRS > 1.2 Thay đổi đã chốt ngày 31/10
### 1.2 Thay đổi đã chốt ngày 31/10

| Thay đổi | Ảnh hưởng |
| --- | --- |
| Đăng ký phải xác thực email qua link | UC01 thêm UC01.1 Xác thực email; tài khoản chưa xác thực không được thử đồ (BR19) |
| Trợ lý gợi ý phối đồ (MVP) | UC mới UC31 Phối đồ với trợ lý; Customer có thêm tool `suggest_outfit` |
| Thử cả set phối đồ (MVP) | UC mới UC32 Thử set phối đồ: tối đa 2 món (trên + dưới), chuẩn bị ảnh tham chiếu của set (UC32.1) rồi chạy thử đồ một lần, tính 1 lượt (BR20) |
| Thử đồ từ trang sản phẩm | Chỉ thử món đang xem (UC12 giữ nguyên) |

Quy tắc mới:

| Mã | Quy tắc |
| --- | --- |
| BR19 | Tài khoản phải xác thực email trước khi thử đồ; link xác thực hết hạn sau 24 giờ, gửi lại được |
| BR20 | Set phối đồ gồm đúng 1 món trên (áo sơ mi/áo kiểu, áo thun, áo len — slot TOP) và 1 món dưới (quần, chân váy — slot BOTTOM); áo khoác là lớp ngoài (slot OTHER), không vào set; đầm liền không vào set; phụ kiện (giày, túi — slot ACCESSORY) không vào set và không thử đồ ảo; cả 2 món phải bật thử đồ và còn hàng; thử set tính 1 lượt ảnh |
| BR21 | Thử qua webcam: chỉ Customer đã xác thực email; tối đa 20 giây mỗi phiên, 1 phiên mỗi ngày; toàn hệ thống có trần ngân sách 250 giây (khoảng 10 USD), hết trần thì ẩn nút webcam cho tới khi Admin nạp thêm; không ghi lại video, ảnh chụp khung hình theo BR16 |

Thử đồ qua webcam được đưa vào MVP với mã UC33 (bổ sung 31/10); các UC giai đoạn 2 (voucher, wishlist) mang mã UC34–UC35.

