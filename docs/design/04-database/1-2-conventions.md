Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 1. Quy ước và quyết định > 1.2 Quy ước
### 1.2 Quy ước

- Tên bảng, cột: tiếng Anh, `snake_case`, bảng số nhiều.
- Ngoại lệ về khóa: bảng nối dùng khóa chính ghép (`cart_items`, `order_items`, `tryon_job_items`); dữ liệu danh mục có mã chính thức dùng mã đó làm khóa (`provinces`, `wards`); `settings` dùng `key`.
- Tiền: `integer`, đơn vị đồng (VND không có phần lẻ). Chi phí AI: `numeric(10,4)` USD.
- Thời gian: `timestamptz`, lưu UTC.
- Giá trị liệt kê: `varchar` + `CHECK`, không dùng kiểu enum của PostgreSQL (thêm giá trị không cần migration phức tạp). Tên giá trị giữ nguyên như B2.
- File (ảnh, video) nằm trên MinIO; bảng chỉ lưu `object_key`, URL sinh lúc đọc.
- Tham chiếu từ schema `ai` sang `core` (người dùng, biến thể sản phẩm) là cột `uuid` không có khóa ngoại (B3, mục 3.5); đánh dấu `ref` trong từ điển dữ liệu.
- Không thêm `updated_at`, xóa mềm hay cột audit chung cho mọi bảng; chỉ bảng nào có UC cần mới có.

