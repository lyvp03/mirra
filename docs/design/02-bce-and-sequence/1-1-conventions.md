Nguồn: 02-BCE-AND-SEQUENCE.md > Mirra — B2: Phân tích BCE và sequence > 1. Quy ước và danh mục lớp phân tích > 1.1 Quy ước
### 1.1 Quy ước

- Tên lớp, thuộc tính, thông điệp trong sơ đồ viết bằng tiếng Anh; mô tả viết tiếng Việt.
- Boundary: màn hình, hộp thoại (đuôi `Screen`, `Form`, `Dialog`, `Widget`) và giao diện tới hệ thống ngoài (đuôi `Boundary`).
- Control: mỗi use case một control (đuôi `Controller`); logic dùng chung tách thành control riêng (đuôi `Policy`, `Calculator`, `Validator`).
- Entity: khái niệm nghiệp vụ có dữ liệu cần lưu (danh từ số ít).
- Actor chỉ gửi thông điệp tới boundary; boundary chỉ gọi control; control gọi entity, boundary hệ thống ngoài và control khác.
- Mỗi UC có một sơ đồ lớp phân tích và một sequence; nhánh thay thế quan trọng vẽ bằng `alt`/`opt`, phần còn lại theo đặc tả ở SRS và B1.
- Các UC con CRUD gộp vào sequence của UC cha, mỗi UC con là một khối `alt`.

