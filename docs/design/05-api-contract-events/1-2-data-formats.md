Nguồn: 05-API-CONTRACT-EVENTS.md > Mirra — B5: API, contract, sự kiện > 1. Quy ước chung > 1.2 Định dạng dữ liệu
### 1.2 Định dạng dữ liệu

| Nội dung | Quy ước |
| --- | --- |
| Body | JSON UTF-8; tên trường `snake_case`, trùng tên cột B4 khi có |
| ID | Chuỗi UUID; đơn hàng có thêm `code` dùng trên URL của khách |
| Thời gian | ISO 8601 UTC có `Z`, ví dụ `2026-11-03T08:15:00Z`; web tự đổi sang giờ Việt Nam |
| Tiền | Số nguyên, đơn vị đồng |
| Giá trị liệt kê | Chuỗi viết hoa như B4 (`AWAITING_PAYMENT`, `SET_IMAGE`…) |
| Ảnh trả về | URL đầy đủ: bucket `products` là URL công khai, bucket `tryon` là URL ký sẵn hạn ngắn |
| Tải file lên | `multipart/form-data`, JPG/PNG/WebP, ≤ 5 MB |

