Nguồn: 03-PACKAGE-COMPONENT-DEPLOYMENT.md > Mirra — B3: Package, Component, Deployment > 3. Ánh xạ lớp B2 vào package > 3.4 Boundary giao diện
### 3.4 Boundary giao diện

| Boundary B2 | Route hoặc component của web |
| --- | --- |
| RegisterForm, LoginForm, PasswordResetForm | `app/(auth)` |
| ProfileScreen, AddressBookScreen | `app/(shop)/account` |
| ProductListScreen, ProductDetailScreen | `app/(shop)/products`, `app/(shop)/products/[slug]` |
| CartScreen, CheckoutScreen, PaymentScreen | `app/(shop)/cart`, `checkout`, `payment/[code]` |
| OrderHistoryScreen, OrderDetailScreen, ReviewForm | `app/(shop)/orders`, `orders/[code]` (Guest mở qua link tra đơn) |
| TryOnScreen, ConsentDialog | `app/(shop)/tryon`, `components/tryon` |
| TryOnHistoryScreen | `app/(shop)/tryon/history` |
| WebcamTryOnScreen | `app/(shop)/webcam`, `components/tryon` |
| ChatWidget, ConfirmationCard | `components/chat`, gắn ở layout chung |
| AdminProductScreen (gồm ẩn đánh giá, tạo nháp AI), AdminInventoryScreen, AdminOrderScreen, AdminFaqScreen, AdminPricingScreen, AdminRefundScreen, AdminCustomerScreen, AdminStaffScreen, ReportScreen, SettingsScreen, TraceViewerScreen | `app/(admin)/admin/*`, mỗi màn một route |

