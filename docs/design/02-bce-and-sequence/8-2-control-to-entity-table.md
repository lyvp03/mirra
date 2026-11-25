Nguồn: 02-BCE-AND-SEQUENCE.md > Mirra — B2: Phân tích BCE và sequence > 8. Sơ đồ lớp phân tích gộp > 8.2 Bảng control → entity
### 8.2 Bảng control → entity

Ký hiệu: C tạo, R đọc, U sửa, D xóa.

Category, SizeChart và AdminUnit không có control tạo: dữ liệu được nạp sẵn bằng seed khi triển khai (chốt ở B3).

| Control | UC | Entity và thao tác |
| --- | --- | --- |
| RegisterController | UC01 | User (C), AuthToken (C, U) |
| LoginController | UC02 | User (R, U), AuthToken (C, U) |
| PasswordResetController | UC03 | User (U), AuthToken (C, U) |
| ProfileController | UC04 | User (R, U), Address (C, R, U, D), AdminUnit (R), AuthToken (U) |
| ProductBrowseController | UC05 | Product, ProductVariant, ProductImage, Promotion, SizeChart (R) |
| CartController | UC06 | Cart (C, R, U), CartItem (C, R, U, D), ProductVariant (R) |
| PlaceOrderController | UC07 | Cart (R, U), Promotion, Address (R), Order, OrderItem, Payment (C) |
| PaymentController | UC08 | Payment (R, U), Order (U) |
| OrderTrackingController | UC09 | Order, OrderItem, OrderStatusHistory, Payment (R) |
| OrderCancelController | UC10 | Order (U), OrderStatusHistory (C), Payment (U) |
| ReviewController | UC11 | Review (C, R, U), Order, OrderItem (R) |
| PhotoTryOnController | UC12 | User (R), PhotoConsent (C, R), UserPhoto (C, R), ProductImage (R), TryOnJob (C, R, U), AICostRecord (C) |
| TryOnVideoController | UC13 | TryOnJob (C, R, U), AICostRecord (C) |
| TryOnHistoryController | UC14 | UserPhoto (C, R, D), TryOnJob (R, D), PhotoConsent (R) |
| ChatController | UC15 | Conversation (C, R, U), ChatMessage (C, R), Setting (R), AICostRecord (C) |
| ActionConfirmationController | UC16 | PendingAction (R, U), Conversation (R) |
| ProductManagementController | UC17 | Category, SizeChart (R), Product, ProductVariant, ProductImage (C, R, U, D), SearchDocument (C, U) |
| ProductDraftController | UC18 | Category (R), AICostRecord (C) |
| InventoryController | UC19 | ProductVariant (R, U), InventoryLedgerEntry (C, R) |
| OrderProcessingController | UC20 | Order (R, U), OrderItem (R), OrderStatusHistory (C), Payment (U) |
| FaqManagementController | UC21 | Faq (C, R, U, D), SearchDocument (C, U, D) |
| PricingController | UC22 | Product (U), ProductVariant, ProductImage (R), Promotion (C, R, U), SearchDocument (U) |
| RefundController | UC23 | Order (U), OrderStatusHistory (C), Payment (R, U) |
| CustomerManagementController | UC24 | User (R, U), Order (R), AuthToken (U) |
| StaffManagementController | UC25 | User (C, R, U), AuthToken (C, U) |
| ReportController | UC26 | Order, OrderItem, TryOnJob, WebcamSession, Conversation, AICostRecord (R) |
| SettingsController | UC27 | Setting (R, U), SettingHistory (C) |
| TraceController | UC28 | Conversation, ChatMessage, PendingAction, AICostRecord (R) |
| OrderExpiryController | UC29 | Order (R, U), Payment (U), OrderStatusHistory (C) |
| PhotoRetentionController | UC30 | UserPhoto (R, U), TryOnJob (R, U) |
| OutfitSuggestionController | UC31 | SearchDocument, ProductImage (R), OutfitSuggestion (C) |
| OutfitTryOnController | UC32 | OutfitSuggestion, ProductVariant, UserPhoto (R), TryOnJob (C, R, U), AICostRecord (C) |
| WebcamTryOnController | UC33 | User, PhotoConsent, ProductImage (R), WebcamSession (C, U), WebcamBudget (C, R, U), TryOnJob (C), AICostRecord (C) |

