Nguồn: 03-PACKAGE-COMPONENT-DEPLOYMENT.md > Mirra — B3: Package, Component, Deployment > 3. Ánh xạ lớp B2 vào package > 3.1 Control
### 3.1 Control

| Control B2 | UC | Service | Lớp thiết kế |
| --- | --- | --- | --- |
| RegisterController, LoginController, PasswordResetController | UC01–UC03 | core\_api | `services.AuthService` |
| ProfileController | UC04 | core\_api | `services.ProfileService` |
| ProductBrowseController, ProductManagementController | UC05, UC17 | core\_api | `services.CatalogService` |
| CartController | UC06 | core\_api | `services.CartService` |
| PlaceOrderController, OrderTrackingController, OrderCancelController, OrderProcessingController | UC07, UC09, UC10, UC20 | core\_api | `services.OrderService` |
| OrderExpiryController | UC29 | core\_worker | `workers.OrderExpiryJob` gọi `OrderService` |
| PaymentController | UC08 | core\_api | `services.PaymentService` |
| RefundController | UC23 | core\_api | `OrderService` (UC23.1), `PaymentService` (UC23.2) |
| InventoryController | UC19 | core\_api | `services.InventoryService` |
| ReviewController | UC11 | core\_api | `services.ReviewService` |
| FaqManagementController | UC21 | core\_api | `services.FaqService` |
| PricingController | UC22 | core\_api | `services.PricingService` |
| CustomerManagementController, StaffManagementController | UC24, UC25 | core\_api | `services.AccountAdminService` |
| ReportController | UC26 | core\_api | `services.ReportService` (+ `AiServiceClient` lấy số liệu AI) |
| SettingsController | UC27 | core\_api | `services.SettingsService` |
| ChatController | UC15 | ai\_service | `services.ChatService` + `agent` |
| ActionConfirmationController | UC16 | ai\_service | `services.ActionService` |
| OutfitSuggestionController | UC31 | ai\_service | `services.OutfitService` (tool `suggest_outfit` gọi) |
| PhotoTryOnController, TryOnVideoController, OutfitTryOnController | UC12, UC13, UC32 | ai\_service | `services.TryOnService`; phần chạy job ở `workers.TryOnJobRunner` (ai\_worker) |
| TryOnHistoryController | UC14 | ai\_service | `services.TryOnHistoryService` |
| PhotoRetentionController | UC30 | ai\_worker | `workers.PhotoRetentionJob` gọi `RetentionService` |
| WebcamTryOnController | UC33 | ai\_service | `services.WebcamService`; phiên bỏ dở do `workers.WebcamSweepJob` xử lý |
| ProductDraftController | UC18 | ai\_service | `services.ProductDraftService` |
| TraceController | UC28 | ai\_service | `services.TraceService` |

