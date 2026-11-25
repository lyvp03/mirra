Nguồn: 06-CLASS-AND-DESIGN-PATTERN.md > Mirra — B6: Thiết kế lớp và design pattern > 8. Thay đổi so với B2–B5
## 8. Thay đổi so với B2–B5

| Chỗ | B6 | Lý do |
| --- | --- | --- |
| `ShippingFeeCalculator` (B2, B3) | Đổi thành interface `ShippingFeeStrategy` + `DistanceTierStrategy` | Thể hiện điểm thay bằng GHN (B1 mục 6.3) |
| `StockPolicy.reserve/release` (B2) | `take` / `give_back` | Tồn trừ ngay khi đặt, cộng lại khi hủy (B4) |
| `AiServiceClient` (B3) | `AiUsageClient` | Chỉ dùng cho báo cáo |
| Lớp mới ở Identity | `OneTimeTokenService`, `LoginThrottle`, `PasswordHasher`, `TokenSigner` | Tách logic token, khóa đăng nhập, băm mật khẩu, ký JWT khỏi `AuthService` |
| Lớp mới ở Catalog | `PriceCalculator`, `PublishPolicy` | Giá hiệu lực tính một chỗ; điều kiện công khai sản phẩm (UC22.1) |
| Lớp mới ở Ordering | `OrderCodeGenerator` | Mã đơn 10 chữ số cho payOS (B5) |
| Lớp mới ở Administration | `SettingSchemaRegistry` | Kiểm giá trị theo B5 mục 7.2 |
| Lớp mới ở ai-service | `AgentRunner`, `SetRule`, `CostRecorder`, `PriceTable`, `TryOnJobRunner` và 3 lớp con, `TryOnJobConsumer`, `WebcamSweepJob` | Cầu nối LangGraph; quy tắc set BR20 dùng chung cho TryOn và Webcam; ghi chi phí; khung job |
| `CostRecorder` | Ở package `core` dùng chung của ai-service | Tránh vòng phụ thuộc với Observability (mục 7.2) |
| Kiểm quyền đánh giá (UC11) | `ReviewRepository.eligible_item` đọc `orders` thay vì gọi Ordering | Tránh vòng Catalog ↔ Ordering |
| Các endpoint chuyển trạng thái đơn (B5 mục 3.3) | Cùng gọi `OrderService.staff_transition` | Quyền theo trạng thái nằm trong `OrderStateMachine` |
| Admin hủy đơn đang giao (UC23.1) | Không tự cộng tồn; hàng về kho ghi bằng điều chỉnh tồn (UC19.2) | Khớp B2 UC23.1: chỉ trả kho khi hàng còn trong kho |
| Ordering (sau rà soát 06/11) | `OrderAccessPolicy`, `OrderRepository.closed_at`, `PaymentGateway.get_status / cancel_link`, `PaymentService.reconcile` | Link Guest có hạn (BR12); webhook payOS bị mất không làm hủy nhầm đơn đã trả; sequence 5.2 vẽ thêm nhánh thanh toán đến muộn đã có ở B2 UC08 |
| core-worker (sau rà soát 06/11) | `BackupJob`, `BackupTarget` | Sao lưu DB + ảnh sản phẩm hằng đêm ra ngoài VPS (B3) |
| ai-service (sau rà soát 06/11) | `CostGuard`, `AICostRecordRepository.sum_by_day / sum_since`, `ImageValidator.strip_metadata` | Trần chi phí AI theo tháng và báo cáo theo ngày (NFR13); bỏ EXIF ảnh người dùng (NFR09) |
| Assistant (theo B7) | `AgentState`, `AgentContext`, `PromptBuilder`, `AgentRunner.resume`, `PendingActionRepository.get_open / upsert` | State, prompt và luật "tin mới thì bỏ thao tác cũ" (B7 mục 2, 3, 5) |
| Guardrail (theo B7) | `InputRules`, `InputClassifier`, `OutputVerifier`; `check_output(text, tool_data)` | Guardrail 4 lớp (B7 mục 6) |
| Tool và job (theo B7) | 12 tool trong `ToolRegistry`, `SizeAdvisor`, `CheckpointCleanupJob`; nháp sản phẩm từ ảnh chỉ còn là nút trên form (`ProductDraftService`), không còn là tool chat | B7 mục 3.6, 4 |

Danh sách tool theo vai trò, cấu trúc graph, prompt, chi tiết `Guardrail` và thời hạn chờ xác nhận của `PendingAction` (10 phút) đã chốt ở [B7](https://claude.ai/artifact/JqesBMTsjrfCLztNEuy1sk); ba dòng cuối bảng trên ghi các lớp B6 thêm vào theo B7.
