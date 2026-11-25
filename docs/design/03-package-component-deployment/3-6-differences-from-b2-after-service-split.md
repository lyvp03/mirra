Nguồn: 03-PACKAGE-COMPONENT-DEPLOYMENT.md > Mirra — B3: Package, Component, Deployment > 3. Ánh xạ lớp B2 vào package > 3.6 Khác biệt so với B2 khi tách service
### 3.6 Khác biệt so với B2 khi tách service

| Ở B2 | Ở B3 | Lý do |
| --- | --- | --- |
| ProductManagementController, FaqManagementController gọi EmbeddingBoundary và ghi SearchDocument | core\_api chỉ phát sự kiện; `IndexSyncConsumer` ở ai\_worker tạo embedding và ghi SearchDocument | SearchDocument thuộc schema `ai`; core không phụ thuộc dịch vụ AI |
| ProductDraftController gọi ProductManagementController để lưu | ai\_service trả bản nháp cho web; Staff sửa rồi web gọi API tạo sản phẩm của core (UC17.1) | Bước lưu luôn qua người duyệt, không cần service gọi service |
| WebcamTryOnController tự giữ chỗ và quyết toán ngân sách | `WebcamBudgetPolicy` trong `domain` | Dùng chung cho API và job dọn phiên |
| ReportController đọc trực tiếp TryOnJob, WebcamSession, Conversation, AICostRecord | `ReportService` lấy các số này từ `UsageService` của ai\_service qua `/internal` | Không đọc chéo schema |
| ChatController đọc Setting (hạn mức chat), TryOnQuotaPolicy đọc Setting | ai\_service lấy cấu hình qua `/internal` của core, đệm trong Redis, làm mới khi có sự kiện cấu hình thay đổi | Setting thuộc schema `core` |

