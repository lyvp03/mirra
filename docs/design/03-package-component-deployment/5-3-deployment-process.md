Nguồn: 03-PACKAGE-COMPONENT-DEPLOYMENT.md > Mirra — B3: Package, Component, Deployment > 5. Sơ đồ deployment > 5.3 Quy trình triển khai
### 5.3 Quy trình triển khai

1. Push lên nhánh chính → GitHub Actions chạy ruff, eslint, test.
2. Build 3 image (`web`, `core`, `ai`), gắn tag theo commit, đẩy lên GHCR.
3. SSH vào VPS: `docker compose pull`, chạy migration từng service (Alembic của core và của ai, mỗi bên một bảng phiên bản trong schema của mình), rồi `docker compose up -d`.
4. Container ứng dụng chờ postgres, redis healthy mới khởi động; mọi service có `/health`, chính sách `restart: unless-stopped`.
5. Lần đầu triển khai chạy lệnh seed: AdminUnit, Category, SizeChart, tài khoản Admin đầu tiên, giá trị Setting mặc định. Seed chạy lại không tạo trùng.

