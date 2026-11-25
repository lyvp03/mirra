Nguồn: 06-CLASS-AND-DESIGN-PATTERN.md > Mirra — B6: Thiết kế lớp và design pattern > 3. core-api
## 3. core-api

Router (tầng api) không vẽ: mỗi router chỉ kiểm DTO của B5, lấy `CurrentUser` và gọi một method service. Lớp nền ở mục 2 cũng không vẽ lại (mọi service dùng `UnitOfWork`).

