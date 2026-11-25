Nguồn: 03-PACKAGE-COMPONENT-DEPLOYMENT.md > Mirra — B3: Package, Component, Deployment > 5. Sơ đồ deployment > 5.6 Sao lưu
### 5.6 Sao lưu

Cả hệ thống nằm trên một VPS, nên bản sao lưu phải nằm **ngoài** VPS thì mới có ích khi máy hỏng.

| Nội dung | Cách làm | Tần suất, lưu giữ |
| --- | --- | --- |
| PostgreSQL (schema `core` + `ai`) | `BackupJob` trong core-worker chạy `pg_dump` bằng user DB `mirra_backup` (chỉ đọc cả hai schema), nén rồi đẩy lên kho S3-compatible ngoài VPS | 02:00 hằng đêm, giữ 7 bản |
| MinIO bucket `products` | Cùng job, mirror bucket sang kho ngoài VPS | 02:00 hằng đêm, giữ 7 bản |
| MinIO bucket `tryon` | **Không sao lưu** | Ảnh người dùng phải xóa sau 30 ngày (BR16, Luật 91/2025); giữ bản sao sẽ trái quy tắc này |
| Redis | Không sao lưu riêng | Chỉ chứa dữ liệu tạm (hàng đợi, idempotency, khóa đăng nhập); AOF đủ cho khởi động lại |

Thông tin truy cập kho sao lưu nằm trong file môi trường trên VPS như các bí mật khác (mục 5.4), chỉ core-worker nhận. Trước buổi bảo vệ thử khôi phục một lần vào môi trường dev: một bản sao lưu chưa từng khôi phục thì chưa chắc dùng được.

