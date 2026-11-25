Nguồn: 02-BCE-AND-SEQUENCE.md > Mirra — B2: Phân tích BCE và sequence > 1. Quy ước và danh mục lớp phân tích > 1.2 Boundary
### 1.2 Boundary

| Lớp | Loại | Dùng ở |
| --- | --- | --- |
| RegisterForm, LoginForm, PasswordResetForm | Màn hình | UC01–UC03 |
| ProfileScreen, AddressBookScreen | Màn hình | UC04 |
| ProductListScreen, ProductDetailScreen | Màn hình | UC05, UC12, UC33 |
| CartScreen, CheckoutScreen, PaymentScreen | Màn hình | UC06–UC08 |
| OrderHistoryScreen, OrderDetailScreen, ReviewForm | Màn hình | UC09–UC11 |
| TryOnScreen, ConsentDialog, TryOnHistoryScreen, WebcamTryOnScreen | Màn hình, hộp thoại | UC12–UC14, UC32, UC33 |
| ChatWidget, ConfirmationCard | Màn hình, hộp thoại | UC15, UC16, UC31 |
| AdminProductScreen, AdminInventoryScreen, AdminOrderScreen, AdminFaqScreen | Màn hình quản trị | UC17–UC21 |
| AdminPricingScreen, AdminRefundScreen, AdminCustomerScreen, AdminStaffScreen | Màn hình quản trị | UC22–UC25 |
| ReportScreen, SettingsScreen, TraceViewerScreen | Màn hình quản trị | UC26–UC28 |
| PaymentGatewayBoundary | Hệ thống ngoài (payOS) | UC07, UC08, UC23, UC29 |
| EmailServiceBoundary | Hệ thống ngoài (SMTP) | Nhiều UC |
| TryOnServiceBoundary | Hệ thống ngoài (thử đồ ảnh, video) | UC12, UC13, UC32 |
| RealtimeTryOnBoundary | Hệ thống ngoài (thử đồ realtime) | UC33 |
| LLMBoundary, EmbeddingBoundary | Hệ thống ngoài (AI) | UC15, UC18, UC21, UC31 |
| TraceStoreBoundary | Hệ thống ngoài (lưu trace AI) | UC15, UC28 |
| SchedulerBoundary | Bộ hẹn giờ (actor thời gian) | UC29, UC30 |

