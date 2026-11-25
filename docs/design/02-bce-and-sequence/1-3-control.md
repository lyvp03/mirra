Nguồn: 02-BCE-AND-SEQUENCE.md > Mirra — B2: Phân tích BCE và sequence > 1. Quy ước và danh mục lớp phân tích > 1.3 Control
### 1.3 Control

| Lớp | UC | Lớp | UC |
| --- | --- | --- | --- |
| RegisterController | UC01 | ProductManagementController | UC17 |
| LoginController | UC02 | ProductDraftController | UC18 |
| PasswordResetController | UC03 | InventoryController | UC19 |
| ProfileController | UC04 | OrderProcessingController | UC20 |
| ProductBrowseController | UC05 | FaqManagementController | UC21 |
| CartController | UC06 | PricingController | UC22 |
| PlaceOrderController | UC07 | RefundController | UC23 |
| PaymentController | UC08 | CustomerManagementController | UC24 |
| OrderTrackingController | UC09 | StaffManagementController | UC25 |
| OrderCancelController | UC10 | ReportController | UC26 |
| ReviewController | UC11 | SettingsController | UC27 |
| PhotoTryOnController | UC12 | TraceController | UC28 |
| TryOnVideoController | UC13 | OrderExpiryController | UC29 |
| TryOnHistoryController | UC14 | PhotoRetentionController | UC30 |
| ChatController | UC15 | OutfitSuggestionController | UC31 |
| ActionConfirmationController | UC16 | OutfitTryOnController | UC32 |
|  |  | WebcamTryOnController | UC33 |

Control dùng chung:

| Lớp | Trách nhiệm | Dùng ở |
| --- | --- | --- |
| ShippingFeeCalculator | Tính phí giao hàng theo khoảng cách, cân nặng, ngưỡng miễn phí | UC07 |
| StockPolicy | Kiểm tra và trừ, hoàn tồn kho, ghi sổ kho | UC07, UC10, UC19, UC20, UC23, UC29 |
| OrderStateMachine | Kiểm tra chuyển trạng thái đơn và thanh toán hợp lệ | UC08, UC10, UC20, UC23, UC29 |
| TryOnQuotaPolicy | Kiểm tra và trừ lượt ảnh, video, phiên webcam, trần ngân sách | UC12, UC13, UC32, UC33 |
| ImageValidator | Kiểm tra ảnh toàn thân, một người, định dạng | UC12, UC14, UC32 |
| OutfitComposer | Chuẩn bị ảnh tham chiếu của set: dùng chung ảnh nếu 2 món chụp cùng ảnh, nếu không thì ghép ảnh tham chiếu 2 món thành một ảnh | UC32, UC33 |
| Guardrail | Kiểm tra tin nhắn vào và câu trả lời ra | UC15, UC31 |
| ToolRegistry | Chọn bộ tool theo vai trò | UC15, UC31 |
| AccessPolicy | Kiểm tra quyền theo vai trò | Mọi UC cần đăng nhập |

