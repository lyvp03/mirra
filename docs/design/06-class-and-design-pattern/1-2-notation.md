Nguồn: 06-CLASS-AND-DESIGN-PATTERN.md > Mirra — B6: Thiết kế lớp và design pattern > 1. Quy ước và quyết định > 1.2 Ký hiệu
### 1.2 Ký hiệu

- Sơ đồ lớp bằng Mermaid `classDiagram`, bạn vẽ lại UML chuẩn trong Astah.
- Kiểu viết theo Python: `str`, `int`, `UUID`, `datetime`, `list~T~`, `T | None`; method bất đồng bộ viết như method thường (code thật dùng `async def`).
- `<<interface>>` là `typing.Protocol`; `<<abstract>>` là lớp cơ sở có method trừu tượng; `<<service>>`, `<<domain>>`, `<<repository>>`, `<<adapter>>`, `<<router>>` chỉ tầng theo B3.
- Mũi tên `..|>` là hiện thực interface, `--|>` là kế thừa, `-->` là phụ thuộc (inject qua constructor), `*--` là thành phần.
- Model ORM trùng tên bảng B4 ở dạng số ít PascalCase (`Order`, `TryOnJob`); thuộc tính xem từ điển dữ liệu B4.

