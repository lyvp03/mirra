Nguồn: 03-PACKAGE-COMPONENT-DEPLOYMENT.md > Mirra — B3: Package, Component, Deployment > 1. Quy ước và quyết định > 1.3 Ranh giới hai service
### 1.3 Ranh giới hai service

- **core-api** sở hữu schema `core`: tài khoản, địa chỉ, danh mục, sản phẩm, giá, giỏ, đơn, thanh toán, kho, đánh giá, FAQ, cấu hình, báo cáo. Là nơi duy nhất ký JWT.
- **ai-service** sở hữu schema `ai`: hội thoại, hành động chờ xác nhận, thử đồ ảnh/video/set, webcam, gợi ý phối đồ, chỉ mục tìm kiếm, chi phí AI, trace.
- Không service nào đọc schema của service kia (2 DB user riêng). Cần dữ liệu của bên kia thì gọi REST: tool của agent gọi API core bằng JWT của người dùng (BR17); việc nội bộ dùng `/internal` + service key.
- Thay đổi sản phẩm, FAQ, cấu hình ở core được phát thành sự kiện Redis Streams; ai-worker tiêu thụ để cập nhật chỉ mục tìm kiếm và bộ nhớ đệm cấu hình.

