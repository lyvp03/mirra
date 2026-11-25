Nguồn: 06-CLASS-AND-DESIGN-PATTERN.md > Mirra — B6: Thiết kế lớp và design pattern > 1. Quy ước và quyết định > 1.3 Quy tắc thiết kế
### 1.3 Quy tắc thiết kế

- Service nhận phụ thuộc qua constructor (FastAPI `Depends` lắp ráp), không tự tạo adapter hay session.
- Một lời gọi service ghi dữ liệu chạy trong một `UnitOfWork`; sự kiện và việc gọi ra ngoài sau commit đăng ký qua `after_commit`.
- Domain là lớp thuần Python, không import FastAPI, SQLAlchemy hay SDK ngoài.
- Service không ném `HTTPException`; ném `AppError(code)` và tầng api đổi thành problem+json (B5 mục 1.4).
- Component khác trong cùng service chỉ gọi nhau qua service, không dùng repository của nhau.

