# INDEX thiết kế Mirra

Sinh tự động bởi `scripts/split_design.py`. Đừng sửa tay.

## 1. Bảng UC

| UC | Tên | 01-uc | 02-bce | 04-db | 05-api | 06-class | 07-ai | 09-test |
|---|---|---|---|---|---|---|---|---|
| UC01 | Đăng ký tài khoản | 01-uc/UC01.md<br>01-uc/1-2-changes-agreed-on-oct-31.md<br>01-uc/2-1-account-management.md<br>01-uc/6-2-agreed-values.md | 02-bce-and-sequence/UC01.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md | 04-database/auth-tokens.md<br>04-database/users.md | 05-api-contract-events/3-1-authentication-and-accounts-identity.md | 06-class-and-design-pattern/3-1-identity-uc01-uc04-uc24-uc25.md |  | 09-testing/sample-test-case-table.md |
| UC02 | Đăng nhập, đăng xuất | 01-uc/UC02.md<br>01-uc/2-1-account-management.md<br>01-uc/6-2-agreed-values.md | 02-bce-and-sequence/UC02.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md | 04-database/auth-tokens.md<br>04-database/users.md | 05-api-contract-events/3-1-authentication-and-accounts-identity.md | 06-class-and-design-pattern/3-1-identity-uc01-uc04-uc24-uc25.md |  | 09-testing/sample-test-case-table.md |
| UC03 | Quên mật khẩu | 01-uc/UC03.md<br>01-uc/2-1-account-management.md<br>01-uc/6-2-agreed-values.md | 02-bce-and-sequence/UC03.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md | 04-database/auth-tokens.md<br>04-database/users.md | 05-api-contract-events/3-1-authentication-and-accounts-identity.md | 06-class-and-design-pattern/3-1-identity-uc01-uc04-uc24-uc25.md |  |  |
| UC04 | Quản lý hồ sơ và sổ địa chỉ | 01-uc/UC04.md<br>01-uc/2-1-account-management.md<br>01-uc/6-2-agreed-values.md | 02-bce-and-sequence/UC04.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md | 04-database/8-1-index.md<br>04-database/addresses.md<br>04-database/provinces-wards.md<br>04-database/users.md | 05-api-contract-events/3-1-authentication-and-accounts-identity.md | 06-class-and-design-pattern/3-1-identity-uc01-uc04-uc24-uc25.md |  |  |
| UC05 | Xem, tìm kiếm sản phẩm | 01-uc/UC05.md<br>01-uc/2-2-shopping-and-payment.md | 02-bce-and-sequence/UC05.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md | 04-database/8-1-index.md<br>04-database/product-images.md<br>04-database/product-variants.md<br>04-database/products.md | 05-api-contract-events/3-2-products-cart-orders-customer-side.md | 06-class-and-design-pattern/3-2-catalog-uc05-uc11-uc17-uc21-uc22.md |  |  |
| UC06 | Quản lý giỏ hàng | 01-uc/UC06.md<br>01-uc/2-2-shopping-and-payment.md<br>01-uc/2-4-virtual-try-on.md<br>01-uc/5-3-outfit-suggestion-and-set-try-on-uc31-uc32.md<br>01-uc/UC02.md<br>01-uc/UC31.md | 02-bce-and-sequence/UC06.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md<br>02-bce-and-sequence/UC31.md | 04-database/cart-items.md<br>04-database/product-variants.md | 05-api-contract-events/3-2-products-cart-orders-customer-side.md | 06-class-and-design-pattern/3-3-ordering-uc06-uc10-uc19-uc20-uc23-uc29.md | 07-ai-agent/8-changes-from-b4-b6.md |  |
| UC07 | Đặt hàng | 01-uc/1-1-conventions.md<br>01-uc/2-2-shopping-and-payment.md<br>01-uc/5-1-order-and-payment-uc07-uc08-uc29.md<br>01-uc/6-2-agreed-values.md | 02-bce-and-sequence/UC07.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md<br>02-bce-and-sequence/8-3-shared-controls.md | 04-database/inventory-ledger.md<br>04-database/order-items.md<br>04-database/orders.md<br>04-database/payments.md<br>04-database/product-variants.md<br>04-database/provinces-wards.md | 05-api-contract-events/3-1-authentication-and-accounts-identity.md<br>05-api-contract-events/3-2-products-cart-orders-customer-side.md<br>05-api-contract-events/5-1-order-and-vietqr-payment-uc07-uc08.md<br>05-api-contract-events/7-2-config-keys-settings-uc27.md | 06-class-and-design-pattern/3-3-ordering-uc06-uc10-uc19-uc20-uc23-uc29.md<br>06-class-and-design-pattern/5-1-place-order-uc07.md |  | 09-testing/sample-test-case-table.md |
| UC08 | Thanh toán VietQR | 01-uc/1-1-conventions.md<br>01-uc/2-2-shopping-and-payment.md<br>01-uc/5-1-order-and-payment-uc07-uc08-uc29.md<br>01-uc/UC29.md | 02-bce-and-sequence/UC08.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md<br>02-bce-and-sequence/8-3-shared-controls.md | 04-database/7-changes-from-b2-entities.md<br>04-database/orders.md<br>04-database/payments.md | 05-api-contract-events/3-2-products-cart-orders-customer-side.md<br>05-api-contract-events/5-1-order-and-vietqr-payment-uc07-uc08.md<br>05-api-contract-events/7-2-config-keys-settings-uc27.md | 06-class-and-design-pattern/3-3-ordering-uc06-uc10-uc19-uc20-uc23-uc29.md<br>06-class-and-design-pattern/5-2-payos-webhook-uc08.md<br>06-class-and-design-pattern/8-changes-from-b2-b5.md |  | 09-testing/sample-test-case-table.md |
| UC09 | Theo dõi đơn hàng | 01-uc/UC09.md<br>01-uc/2-2-shopping-and-payment.md | 02-bce-and-sequence/UC09.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md | 04-database/8-1-index.md<br>04-database/order-items.md<br>04-database/order-status-history.md<br>04-database/orders.md | 05-api-contract-events/3-2-products-cart-orders-customer-side.md | 06-class-and-design-pattern/3-3-ordering-uc06-uc10-uc19-uc20-uc23-uc29.md |  |  |
| UC10 | Hủy đơn hàng | 01-uc/UC10.md<br>01-uc/2-2-shopping-and-payment.md | 02-bce-and-sequence/UC10.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md<br>02-bce-and-sequence/8-3-shared-controls.md | 04-database/inventory-ledger.md<br>04-database/order-status-history.md<br>04-database/orders.md | 05-api-contract-events/3-2-products-cart-orders-customer-side.md | 06-class-and-design-pattern/3-3-ordering-uc06-uc10-uc19-uc20-uc23-uc29.md |  |  |
| UC11 | Đánh giá sản phẩm | 01-uc/UC11.md<br>01-uc/2-2-shopping-and-payment.md | 02-bce-and-sequence/UC11.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md | 04-database/order-items.md<br>04-database/reviews.md | 05-api-contract-events/3-2-products-cart-orders-customer-side.md<br>05-api-contract-events/3-3-operations-staff.md | 06-class-and-design-pattern/3-2-catalog-uc05-uc11-uc17-uc21-uc22.md<br>06-class-and-design-pattern/8-changes-from-b2-b5.md |  |  |
| UC12 | Thử đồ bằng ảnh | 01-uc/1-1-conventions.md<br>01-uc/1-2-changes-agreed-on-oct-31.md<br>01-uc/2-4-virtual-try-on.md<br>01-uc/5-2-photo-try-on-uc12.md<br>01-uc/6-2-agreed-values.md<br>01-uc/UC31.md<br>01-uc/UC32.md<br>01-uc/UC33.md | 02-bce-and-sequence/UC12.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md<br>02-bce-and-sequence/8-3-shared-controls.md<br>02-bce-and-sequence/UC32.md<br>02-bce-and-sequence/UC33.md | 04-database/photo-consents.md<br>04-database/product-images.md<br>04-database/tryon-job-items.md<br>04-database/tryon-jobs.md<br>04-database/user-photos.md | 05-api-contract-events/4-1-ai-service-public-ai-v1.md<br>05-api-contract-events/5-3-photo-set-and-video-try-on-uc12-uc13-uc14-uc32.md<br>05-api-contract-events/7-2-config-keys-settings-uc27.md | 06-class-and-design-pattern/4-2-tryon-uc12-uc14-uc30-uc32-and-ai-worker.md<br>06-class-and-design-pattern/5-4-set-try-on-via-job-uc32-uc12-same-without-compositing.md |  | 09-testing/sample-test-case-table.md<br>09-testing/test-case-design-techniques.md |
| UC13 | Tạo video thử đồ | 01-uc/1-1-conventions.md<br>01-uc/2-4-virtual-try-on.md<br>01-uc/UC32.md | 02-bce-and-sequence/UC13.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md<br>02-bce-and-sequence/8-3-shared-controls.md | 04-database/tryon-jobs.md | 05-api-contract-events/4-1-ai-service-public-ai-v1.md<br>05-api-contract-events/5-3-photo-set-and-video-try-on-uc12-uc13-uc14-uc32.md<br>05-api-contract-events/7-2-config-keys-settings-uc27.md | 06-class-and-design-pattern/4-2-tryon-uc12-uc14-uc30-uc32-and-ai-worker.md |  |  |
| UC14 | Quản lý ảnh và lịch sử thử đồ | 01-uc/UC14.md<br>01-uc/2-4-virtual-try-on.md | 02-bce-and-sequence/UC14.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md<br>02-bce-and-sequence/8-3-shared-controls.md | 04-database/8-1-index.md<br>04-database/8-2-delete-rules.md<br>04-database/tryon-jobs.md<br>04-database/user-photos.md | 05-api-contract-events/4-1-ai-service-public-ai-v1.md<br>05-api-contract-events/5-3-photo-set-and-video-try-on-uc12-uc13-uc14-uc32.md<br>05-api-contract-events/7-2-config-keys-settings-uc27.md | 06-class-and-design-pattern/4-2-tryon-uc12-uc14-uc30-uc32-and-ai-worker.md |  |  |
| UC15 | Trò chuyện với trợ lý | 01-uc/1-1-conventions.md<br>01-uc/2-3-chat-with-ai-assistant.md<br>01-uc/5-4-assistant-confirms-write-action-uc15-uc16.md<br>01-uc/6-2-agreed-values.md<br>01-uc/UC31.md | 02-bce-and-sequence/UC15.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md<br>02-bce-and-sequence/8-3-shared-controls.md | 04-database/chat-messages.md<br>04-database/conversations.md<br>04-database/search-documents.md | 05-api-contract-events/4-1-ai-service-public-ai-v1.md<br>05-api-contract-events/5-2-assistant-chat-and-action-confirmation-uc15-uc16-uc31.md<br>05-api-contract-events/7-2-config-keys-settings-uc27.md | 06-class-and-design-pattern/4-1-assistant-uc15-uc16-uc31.md<br>06-class-and-design-pattern/5-3-chat-and-action-confirmation-uc15-uc16.md |  | 09-testing/sample-test-case-table.md |
| UC16 | Xác nhận thao tác của trợ lý | 01-uc/2-3-chat-with-ai-assistant.md<br>01-uc/5-4-assistant-confirms-write-action-uc15-uc16.md<br>01-uc/UC31.md | 02-bce-and-sequence/UC16.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md<br>02-bce-and-sequence/8-3-shared-controls.md<br>02-bce-and-sequence/UC15.md<br>02-bce-and-sequence/UC31.md | 04-database/pending-actions.md | 05-api-contract-events/4-1-ai-service-public-ai-v1.md<br>05-api-contract-events/5-2-assistant-chat-and-action-confirmation-uc15-uc16-uc31.md | 06-class-and-design-pattern/4-1-assistant-uc15-uc16-uc31.md<br>06-class-and-design-pattern/5-3-chat-and-action-confirmation-uc15-uc16.md | 07-ai-agent/8-changes-from-b4-b6.md | 09-testing/sample-test-case-table.md |
| UC17 | Quản lý sản phẩm | 01-uc/UC17.md<br>01-uc/1-1-conventions.md<br>01-uc/2-5-store-operations.md<br>01-uc/6-2-agreed-values.md | 02-bce-and-sequence/UC17.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md<br>02-bce-and-sequence/8-3-shared-controls.md<br>02-bce-and-sequence/UC18.md | 04-database/product-images.md<br>04-database/product-variants.md<br>04-database/products.md | 05-api-contract-events/3-3-operations-staff.md | 06-class-and-design-pattern/3-2-catalog-uc05-uc11-uc17-uc21-uc22.md |  |  |
| UC18 | Tạo sản phẩm nháp bằng AI | 01-uc/1-1-conventions.md<br>01-uc/2-5-store-operations.md | 02-bce-and-sequence/UC18.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md<br>02-bce-and-sequence/8-3-shared-controls.md | 04-database/products.md | 05-api-contract-events/4-1-ai-service-public-ai-v1.md<br>05-api-contract-events/7-1-error-codes.md | 06-class-and-design-pattern/4-4-knowledge-semantic-search-uc18.md |  |  |
| UC19 | Quản lý tồn kho | 01-uc/UC19.md<br>01-uc/2-5-store-operations.md<br>01-uc/6-2-agreed-values.md | 02-bce-and-sequence/UC19.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md<br>02-bce-and-sequence/8-3-shared-controls.md | 04-database/7-changes-from-b2-entities.md<br>04-database/8-1-index.md<br>04-database/inventory-ledger.md<br>04-database/product-variants.md | 05-api-contract-events/3-3-operations-staff.md<br>05-api-contract-events/7-2-config-keys-settings-uc27.md | 06-class-and-design-pattern/3-3-ordering-uc06-uc10-uc19-uc20-uc23-uc29.md<br>06-class-and-design-pattern/8-changes-from-b2-b5.md |  |  |
| UC20 | Xử lý đơn hàng | 01-uc/UC20.md<br>01-uc/1-1-conventions.md<br>01-uc/2-5-store-operations.md | 02-bce-and-sequence/UC20.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md<br>02-bce-and-sequence/8-3-shared-controls.md | 04-database/8-1-index.md<br>04-database/inventory-ledger.md<br>04-database/order-status-history.md<br>04-database/orders.md<br>04-database/payments.md | 05-api-contract-events/3-3-operations-staff.md | 06-class-and-design-pattern/3-3-ordering-uc06-uc10-uc19-uc20-uc23-uc29.md |  | 09-testing/sample-test-case-table.md |
| UC21 | Quản lý FAQ và chính sách | 01-uc/UC21.md<br>01-uc/2-5-store-operations.md | 02-bce-and-sequence/UC21.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md | 04-database/faqs.md | 05-api-contract-events/3-3-operations-staff.md | 06-class-and-design-pattern/3-2-catalog-uc05-uc11-uc17-uc21-uc22.md |  |  |
| UC22 | Quản lý giá và khuyến mãi | 01-uc/UC22.md<br>01-uc/2-6-system-administration.md | 02-bce-and-sequence/UC22.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md<br>02-bce-and-sequence/UC17.md | 04-database/products.md<br>04-database/promotions.md | 05-api-contract-events/3-4-administration-admin.md | 06-class-and-design-pattern/3-2-catalog-uc05-uc11-uc17-uc21-uc22.md<br>06-class-and-design-pattern/8-changes-from-b2-b5.md |  |  |
| UC23 | Hủy đơn đã xác nhận và hoàn tiền | 01-uc/UC23.md<br>01-uc/2-6-system-administration.md<br>01-uc/UC10.md | 02-bce-and-sequence/UC23.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md<br>02-bce-and-sequence/8-3-shared-controls.md<br>02-bce-and-sequence/UC20.md | 04-database/7-changes-from-b2-entities.md<br>04-database/inventory-ledger.md<br>04-database/order-status-history.md<br>04-database/orders.md<br>04-database/payments.md | 05-api-contract-events/3-3-operations-staff.md<br>05-api-contract-events/3-4-administration-admin.md | 06-class-and-design-pattern/3-3-ordering-uc06-uc10-uc19-uc20-uc23-uc29.md<br>06-class-and-design-pattern/8-changes-from-b2-b5.md | 07-ai-agent/4-6-two-write-tools.md | 09-testing/sample-test-case-table.md |
| UC24 | Quản lý khách hàng | 01-uc/UC24.md<br>01-uc/2-6-system-administration.md | 02-bce-and-sequence/UC24.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md | 04-database/7-changes-from-b2-entities.md<br>04-database/8-1-index.md<br>04-database/users.md | 05-api-contract-events/2-1-access-and-refresh-tokens.md<br>05-api-contract-events/3-4-administration-admin.md | 06-class-and-design-pattern/3-1-identity-uc01-uc04-uc24-uc25.md |  |  |
| UC25 | Quản lý nhân viên | 01-uc/2-6-system-administration.md<br>01-uc/UC24.md | 02-bce-and-sequence/UC25.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md | 04-database/8-1-index.md<br>04-database/auth-tokens.md<br>04-database/users.md | 05-api-contract-events/2-1-access-and-refresh-tokens.md<br>05-api-contract-events/3-1-authentication-and-accounts-identity.md<br>05-api-contract-events/3-4-administration-admin.md | 06-class-and-design-pattern/3-1-identity-uc01-uc04-uc24-uc25.md |  |  |
| UC26 | Xem báo cáo | 01-uc/UC26.md<br>01-uc/2-6-system-administration.md | 02-bce-and-sequence/UC26.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md | 04-database/8-1-index.md<br>04-database/ai-cost-records.md | 05-api-contract-events/3-4-administration-admin.md<br>05-api-contract-events/4-3-ai-service-internal-internal-v1-service.md<br>05-api-contract-events/7-2-config-keys-settings-uc27.md | 06-class-and-design-pattern/3-4-administration-uc26-uc27.md<br>06-class-and-design-pattern/4-5-observability-uc26-uc28.md<br>06-class-and-design-pattern/7-2-accepted-exceptions.md |  |  |
| UC27 | Cấu hình hệ thống | 01-uc/UC27.md<br>01-uc/2-6-system-administration.md<br>01-uc/6-2-agreed-values.md<br>01-uc/6-3-distance-based-shipping-fee-heuristic.md | 02-bce-and-sequence/UC27.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md | 04-database/settings-setting-history.md | 05-api-contract-events/3-4-administration-admin.md<br>05-api-contract-events/7-2-config-keys-settings-uc27.md | 06-class-and-design-pattern/3-4-administration-uc26-uc27.md |  |  |
| UC28 | Xem trace của trợ lý | 01-uc/UC28.md<br>01-uc/2-6-system-administration.md | 02-bce-and-sequence/UC28.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md | 04-database/7-changes-from-b2-entities.md<br>04-database/8-1-index.md<br>04-database/ai-cost-records.md<br>04-database/chat-messages.md<br>04-database/conversations.md | 05-api-contract-events/4-1-ai-service-public-ai-v1.md<br>05-api-contract-events/6-4-opentelemetry-and-langfuse.md | 06-class-and-design-pattern/4-5-observability-uc26-uc28.md | 07-ai-agent/2-2-where-data-lives.md<br>07-ai-agent/6-3-layer-1-input.md<br>07-ai-agent/6-5-layer-3-output.md |  |
| UC29 | Tự hủy đơn quá hạn | 01-uc/UC29.md<br>01-uc/2-2-shopping-and-payment.md<br>01-uc/5-1-order-and-payment-uc07-uc08-uc29.md | 02-bce-and-sequence/UC29.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md<br>02-bce-and-sequence/8-3-shared-controls.md | 04-database/8-1-index.md<br>04-database/order-status-history.md<br>04-database/orders.md | 05-api-contract-events/7-2-config-keys-settings-uc27.md | 06-class-and-design-pattern/3-3-ordering-uc06-uc10-uc19-uc20-uc23-uc29.md |  | 09-testing/sample-test-case-table.md |
| UC30 | Tự xóa ảnh quá hạn | 01-uc/UC30.md<br>01-uc/2-4-virtual-try-on.md | 02-bce-and-sequence/UC30.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md | 04-database/8-1-index.md<br>04-database/8-2-delete-rules.md<br>04-database/tryon-jobs.md<br>04-database/user-photos.md | 05-api-contract-events/7-2-config-keys-settings-uc27.md | 06-class-and-design-pattern/4-2-tryon-uc12-uc14-uc30-uc32-and-ai-worker.md |  |  |
| UC31 | Phối đồ với trợ lý | 01-uc/UC31.md<br>01-uc/1-2-changes-agreed-on-oct-31.md<br>01-uc/2-3-chat-with-ai-assistant.md<br>01-uc/5-3-outfit-suggestion-and-set-try-on-uc31-uc32.md<br>01-uc/6-2-agreed-values.md<br>01-uc/UC32.md | 02-bce-and-sequence/UC31.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md<br>02-bce-and-sequence/UC32.md | 04-database/outfit-suggestions.md<br>04-database/search-documents.md | 05-api-contract-events/4-1-ai-service-public-ai-v1.md<br>05-api-contract-events/5-2-assistant-chat-and-action-confirmation-uc15-uc16-uc31.md | 06-class-and-design-pattern/4-1-assistant-uc15-uc16-uc31.md | 07-ai-agent/8-changes-from-b4-b6.md | 09-testing/sample-test-case-table.md |
| UC32 | Thử set phối đồ | 01-uc/UC32.md<br>01-uc/1-2-changes-agreed-on-oct-31.md<br>01-uc/2-3-chat-with-ai-assistant.md<br>01-uc/2-4-virtual-try-on.md<br>01-uc/5-3-outfit-suggestion-and-set-try-on-uc31-uc32.md<br>01-uc/UC31.md<br>01-uc/UC33.md | 02-bce-and-sequence/UC32.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md<br>02-bce-and-sequence/8-3-shared-controls.md | 04-database/outfit-suggestions.md<br>04-database/tryon-job-items.md<br>04-database/tryon-jobs.md | 05-api-contract-events/4-1-ai-service-public-ai-v1.md<br>05-api-contract-events/5-2-assistant-chat-and-action-confirmation-uc15-uc16-uc31.md<br>05-api-contract-events/5-3-photo-set-and-video-try-on-uc12-uc13-uc14-uc32.md<br>05-api-contract-events/7-2-config-keys-settings-uc27.md | 06-class-and-design-pattern/4-2-tryon-uc12-uc14-uc30-uc32-and-ai-worker.md<br>06-class-and-design-pattern/5-4-set-try-on-via-job-uc32-uc12-same-without-compositing.md | 07-ai-agent/4-3-general-conventions.md | 09-testing/sample-test-case-table.md |
| UC33 | Thử đồ qua webcam | 01-uc/UC33.md<br>01-uc/1-2-changes-agreed-on-oct-31.md<br>01-uc/2-4-virtual-try-on.md<br>01-uc/5-5-webcam-try-on-uc33.md | 02-bce-and-sequence/UC33.md<br>02-bce-and-sequence/1-2-boundary.md<br>02-bce-and-sequence/1-3-control.md<br>02-bce-and-sequence/8-2-control-to-entity-table.md<br>02-bce-and-sequence/8-3-shared-controls.md | 04-database/tryon-jobs.md<br>04-database/webcam-sessions.md | 05-api-contract-events/4-1-ai-service-public-ai-v1.md<br>05-api-contract-events/5-2-assistant-chat-and-action-confirmation-uc15-uc16-uc31.md<br>05-api-contract-events/5-4-webcam-try-on-uc33.md<br>05-api-contract-events/7-2-config-keys-settings-uc27.md | 06-class-and-design-pattern/4-3-webcam-uc33.md<br>06-class-and-design-pattern/5-5-open-and-close-webcam-session-uc33.md |  |  |
| UC34 |  | 01-uc/1-2-changes-agreed-on-oct-31.md |  |  |  |  |  |  |
| UC35 |  | 01-uc/1-2-changes-agreed-on-oct-31.md |  |  |  |  |  |  |

## 2. Bảng file

| File | Dòng | Câu đầu |
|---|---|---|
| 01-uc/_overview.md | 7 | Oct 31, 2026 · @Ly |
| 01-uc/1-conventions-and-changes-from-srs.md | 5 | Tài liệu này phân rã 33 use case thành UC con, đặc tả các UC chưa có trong SRS và vẽ activity diagram cho 5 luồng chí… |
| 01-uc/1-1-conventions.md | 8 | UC con đánh mã theo UC cha: UC17.1, UC17.2… |
| 01-uc/1-2-changes-agreed-on-oct-31.md | 20 | Thay đổi / Ảnh hưởng |
| 01-uc/2-use-case-decomposition.md | 5 | Mỗi nhóm có một sơ đồ phân rã và một bảng UC con; mũi tên nét đứt «extend» đi từ UC mở rộng tới UC gốc, «include» đi… |
| 01-uc/2-1-account-management.md | 21 | flowchart LR |
| 01-uc/2-2-shopping-and-payment.md | 36 | flowchart LR |
| 01-uc/2-3-chat-with-ai-assistant.md | 23 | flowchart LR |
| 01-uc/2-4-virtual-try-on.md | 45 | flowchart LR |
| 01-uc/2-5-store-operations.md | 33 | flowchart LR |
| 01-uc/2-6-system-administration.md | 32 | flowchart LR |
| 01-uc/3-business-use-case-specs.md | 5 | Mục này đặc tả mọi UC có luồng nghiệp vụ mà SRS chưa có, bắt đầu từ 2 UC mới. |
| 01-uc/UC31.md | 25 | Mục / Nội dung |
| 01-uc/UC32.md | 27 | Mục / Nội dung |
| 01-uc/UC33.md | 31 | Mục / Nội dung |
| 01-uc/UC01.md | 17 | Mục / Nội dung |
| 01-uc/UC02.md | 11 | Người dùng nhập email và mật khẩu. |
| 01-uc/UC03.md | 6 | Người dùng nhập email; hệ thống luôn báo "nếu email tồn tại, link đã được gửi". |
| 01-uc/UC05.md | 10 | Khách nhập từ khóa hoặc mở danh mục; hệ thống tìm full-text không dấu trên tên, mô tả, tag theo ngôn ngữ đang chọn. |
| 01-uc/UC06.md | 10 | Khách chọn màu, size, số lượng và thêm vào giỏ; Guest lưu ở trình duyệt, Customer lưu trên server. |
| 01-uc/UC09.md | 9 | Customer mở "Đơn của tôi": danh sách đơn mới nhất trước, lọc theo trạng thái. |
| 01-uc/UC10.md | 9 | Khách bấm "Hủy đơn" khi đơn còn Chờ thanh toán hoặc Chờ xác nhận, chọn lý do. |
| 01-uc/UC11.md | 6 | Với đơn Hoàn thành, Customer chấm 1–5 sao và viết nhận xét cho từng món, mỗi món trong đơn đánh giá một lần. |
| 01-uc/UC23.md | 10 | UC23.1: Admin mở đơn Đã xác nhận hoặc Đang giao, chọn "Hủy đơn", nhập lý do. |
| 01-uc/UC26.md | 9 | Admin chọn khoảng thời gian. |
| 01-uc/UC28.md | 5 | Admin tìm hội thoại theo người dùng hoặc thời gian; hệ thống mở trace tương ứng trên Langfuse (tool đã gọi, token, độ… |
| 01-uc/UC29.md | 8 | Mỗi phút, core-worker tìm đơn VietQR ở Chờ thanh toán quá 15 phút. |
| 01-uc/UC30.md | 6 | Mỗi ngày, ai-worker tìm ảnh người dùng và ảnh, video kết quả quá 30 ngày. |
| 01-uc/4-merged-management-use-case-specs.md | 5 | Mỗi nhóm quản lý có một bảng: mỗi dòng là một UC con với dữ liệu vào, kiểm tra và kết quả. |
| 01-uc/UC04.md | 9 | UC con / Dữ liệu vào / Kiểm tra / Kết quả |
| 01-uc/UC14.md | 8 | UC con / Dữ liệu vào / Kiểm tra / Kết quả |
| 01-uc/UC17.md | 10 | UC con / Dữ liệu vào / Kiểm tra / Kết quả |
| 01-uc/UC19.md | 9 | UC con / Dữ liệu vào / Kiểm tra / Kết quả |
| 01-uc/UC20.md | 15 | Luồng đầy đủ ở SRS; bảng dưới chỉ tóm tắt từng UC con. |
| 01-uc/UC21.md | 7 | UC con / Dữ liệu vào / Kiểm tra / Kết quả |
| 01-uc/UC22.md | 8 | UC con / Dữ liệu vào / Kiểm tra / Kết quả |
| 01-uc/UC24.md | 9 | UC con / Dữ liệu vào / Kiểm tra / Kết quả |
| 01-uc/UC27.md | 12 | Nhóm cấu hình / Giá trị / Mặc định |
| 01-uc/5-activity-diagram.md | 5 | Năm luồng dưới đây có nhiều nhánh và nhiều bên tham gia nhất; mỗi làn là một tác nhân hoặc thành phần hệ thống, dùng… |
| 01-uc/5-1-order-and-payment-uc07-uc08-uc29.md | 40 | flowchart TD |
| 01-uc/5-2-photo-try-on-uc12.md | 42 | flowchart TD |
| 01-uc/5-3-outfit-suggestion-and-set-try-on-uc31-uc32.md | 37 | flowchart TD |
| 01-uc/5-4-assistant-confirms-write-action-uc15-uc16.md | 38 | flowchart TD |
| 01-uc/5-5-webcam-try-on-uc33.md | 33 | flowchart TD |
| 01-uc/6-assumptions-to-verify-and-agreed-values.md | 5 | Ba giả định kỹ thuật cần kiểm tra trong benchmark; mười giá trị cấu hình dưới đây đã chốt ngày 31/10. |
| 01-uc/6-1-technical-assumptions.md | 8 | [ ] Thử set bằng ảnh ghép: dịch vụ thử đồ nhận một ảnh ghép 2 món và mặc đúng cả 2 món trong một lần chạy. |
| 01-uc/6-2-agreed-values.md | 21 | Giá trị / Giá trị / Dùng ở |
| 01-uc/6-3-distance-based-shipping-fee-heuristic.md | 29 | Phí ship tính theo khoảng cách từ kho (khu vực Hoàng Mai, Hà Nội; Admin cấu hình được) tới địa chỉ nhận, cộng phụ phí… |
| 02-bce-and-sequence/_overview.md | 7 | Oct 31, 2026 · @Ly |
| 02-bce-and-sequence/1-conventions-and-analysis-class-catalog.md | 5 | Tài liệu phân tích cả 33 use case theo mô hình Boundary–Control–Entity, độc lập công nghệ: không thể hiện core-api, a… |
| 02-bce-and-sequence/1-1-conventions.md | 11 | Tên lớp, thuộc tính, thông điệp trong sơ đồ viết bằng tiếng Anh; mô tả viết tiếng Việt. |
| 02-bce-and-sequence/1-2-boundary.md | 23 | Lớp / Loại / Dùng ở |
| 02-bce-and-sequence/1-3-control.md | 37 | Lớp / UC / Lớp / UC |
| 02-bce-and-sequence/1-4-entity.md | 33 | Lớp / Mô tả |
| 02-bce-and-sequence/2-account-group.md | 3 |  |
| 02-bce-and-sequence/UC01.md | 53 | classDiagram |
| 02-bce-and-sequence/UC02.md | 50 | classDiagram |
| 02-bce-and-sequence/UC03.md | 46 | classDiagram |
| 02-bce-and-sequence/UC04.md | 60 | classDiagram |
| 02-bce-and-sequence/3-shopping-group.md | 3 |  |
| 02-bce-and-sequence/UC05.md | 55 | classDiagram |
| 02-bce-and-sequence/UC06.md | 52 | classDiagram |
| 02-bce-and-sequence/UC07.md | 83 | classDiagram |
| 02-bce-and-sequence/UC08.md | 64 | classDiagram |
| 02-bce-and-sequence/UC09.md | 58 | classDiagram |
| 02-bce-and-sequence/UC10.md | 51 | classDiagram |
| 02-bce-and-sequence/UC11.md | 42 | classDiagram |
| 02-bce-and-sequence/UC29.md | 59 | classDiagram |
| 02-bce-and-sequence/4-ai-assistant-group.md | 5 | Ở mức phân tích, mỗi tool của trợ lý được xem là một lời gọi tới control nghiệp vụ có sẵn (ví dụ search_products gọi… |
| 02-bce-and-sequence/UC15.md | 77 | classDiagram |
| 02-bce-and-sequence/UC16.md | 52 | classDiagram |
| 02-bce-and-sequence/UC31.md | 74 | classDiagram |
| 02-bce-and-sequence/5-virtual-try-on-group.md | 3 |  |
| 02-bce-and-sequence/UC12.md | 91 | classDiagram |
| 02-bce-and-sequence/UC13.md | 48 | classDiagram |
| 02-bce-and-sequence/UC14.md | 59 | classDiagram |
| 02-bce-and-sequence/UC30.md | 32 | classDiagram |
| 02-bce-and-sequence/UC32.md | 82 | Mở từ thẻ set trong chat (UC31). |
| 02-bce-and-sequence/UC33.md | 93 | Mở từ trang chi tiết sản phẩm hoặc từ thẻ sản phẩm/set trong chat. |
| 02-bce-and-sequence/6-operations-group.md | 3 |  |
| 02-bce-and-sequence/UC17.md | 76 | Sản phẩm do Staff tạo luôn ở trạng thái ẩn cho tới khi Admin đặt giá và công khai (UC22.1). |
| 02-bce-and-sequence/UC18.md | 45 | classDiagram |
| 02-bce-and-sequence/UC19.md | 51 | classDiagram |
| 02-bce-and-sequence/UC20.md | 86 | classDiagram |
| 02-bce-and-sequence/UC21.md | 40 | classDiagram |
| 02-bce-and-sequence/7-administration-group.md | 3 |  |
| 02-bce-and-sequence/UC22.md | 59 | classDiagram |
| 02-bce-and-sequence/UC23.md | 67 | classDiagram |
| 02-bce-and-sequence/UC24.md | 41 | classDiagram |
| 02-bce-and-sequence/UC25.md | 50 | classDiagram |
| 02-bce-and-sequence/UC26.md | 49 | classDiagram |
| 02-bce-and-sequence/UC27.md | 37 | classDiagram |
| 02-bce-and-sequence/UC28.md | 45 | classDiagram |
| 02-bce-and-sequence/8-merged-analysis-class-diagram.md | 3 |  |
| 02-bce-and-sequence/8-1-merged-entity-classes.md | 240 | Gộp toàn bộ lớp entity từ các mục 2–7, kèm thuộc tính chính và bội số quan hệ. |
| 02-bce-and-sequence/8-2-control-to-entity-table.md | 43 | Ký hiệu: C tạo, R đọc, U sửa, D xóa. |
| 02-bce-and-sequence/8-3-shared-controls.md | 14 | Control / Được gọi từ / Entity và thao tác / Vai trò |
| 03-package-component-deployment/_overview.md | 7 | Oct 31, 2026 · @Ly |
| 03-package-component-deployment/1-conventions-and-decisions.md | 5 | B3 chuyển kết quả phân tích BCE ở B2 sang cấu trúc vật lý: lớp nào nằm ở service nào, package nào, các thành phần gia… |
| 03-package-component-deployment/1-1-decisions-from-survey.md | 11 | Nội dung / Quyết định |
| 03-package-component-deployment/1-2-mapping-rules-from-b2.md | 12 | Lớp B2 / Đích trong thiết kế |
| 03-package-component-deployment/1-3-two-service-boundary.md | 8 | core-api sở hữu schema core: tài khoản, địa chỉ, danh mục, sản phẩm, giá, giỏ, đơn, thanh toán, kho, đánh giá, FAQ, c… |
| 03-package-component-deployment/1-4-dependency-rules.md | 8 | Tầng trên chỉ gọi tầng ngay dưới hoặc domain; không gọi ngược lên. |
| 03-package-component-deployment/2-package-diagram.md | 3 |  |
| 03-package-component-deployment/2-1-service-level-packages.md | 21 | Bốn package ứng với bốn đơn vị triển khai. |
| 03-package-component-deployment/2-2-core-api.md | 34 | flowchart TB |
| 03-package-component-deployment/2-3-ai-service.md | 38 | flowchart TB |
| 03-package-component-deployment/2-4-web.md | 32 | flowchart TB |
| 03-package-component-deployment/3-mapping-b2-classes-to-packages.md | 3 |  |
| 03-package-component-deployment/3-1-control.md | 30 | Control B2 / UC / Service / Lớp thiết kế |
| 03-package-component-deployment/3-2-shared-controls.md | 11 | Control B2 / Service / Package |
| 03-package-component-deployment/3-3-external-system-boundaries.md | 14 | Boundary B2 / Service / Interface → adapter |
| 03-package-component-deployment/3-4-ui-boundaries.md | 16 | Boundary B2 / Route hoặc component của web |
| 03-package-component-deployment/3-5-entity.md | 10 | Schema / Entity / Lưu file |
| 03-package-component-deployment/3-6-differences-from-b2-after-service-split.md | 11 | Ở B2 / Ở B3 / Lý do |
| 03-package-component-deployment/4-component-diagram.md | 5 | Vòng tròn là interface; mũi tên từ interface vào component là component cung cấp nó, mũi tên từ component ra interfac… |
| 03-package-component-deployment/4-1-system-components.md | 29 | flowchart LR |
| 03-package-component-deployment/4-2-inside-core-api.md | 39 | flowchart LR |
| 03-package-component-deployment/4-3-inside-ai-service.md | 46 | flowchart LR |
| 03-package-component-deployment/4-4-synchronous-interfaces.md | 16 | Tiền tố đường dẫn dưới đây là quy ước; danh sách endpoint, request, response chi tiết ở B5. |
| 03-package-component-deployment/4-5-asynchronous-channels-via-redis.md | 13 | Kênh / Kiểu / Bên ghi / Bên đọc / Dùng cho |
| 03-package-component-deployment/5-deployment-diagram.md | 3 |  |
| 03-package-component-deployment/5-1-production.md | 49 | flowchart TB |
| 03-package-component-deployment/5-2-container.md | 18 | Container / Image / Vai trò / Mạng / Cổng / Volume |
| 03-package-component-deployment/5-3-deployment-process.md | 9 | Push lên nhánh chính → GitHub Actions chạy ruff, eslint, test. |
| 03-package-component-deployment/5-4-config-and-secrets.md | 14 | Bí mật nằm trong file môi trường trên VPS, không đưa vào git. |
| 03-package-component-deployment/5-5-dev-environment.md | 10 | Cùng file Compose cộng một file override cho máy cá nhân: |
| 03-package-component-deployment/5-6-backup.md | 14 | Cả hệ thống nằm trên một VPS, nên bản sao lưu phải nằm ngoài VPS thì mới có ích khi máy hỏng. |
| 03-package-component-deployment/6-assumptions-and-points-to-verify.md | 10 | Giả định / Ảnh hưởng nếu sai / Kiểm chứng |
| 04-database/_overview.md | 7 | Oct 31, 2026 · @Ly |
| 04-database/1-conventions-and-decisions.md | 5 | B4 chuyển entity của B2 thành bảng PostgreSQL 17 theo chuẩn 3NF, chia hai schema theo ranh giới service ở B3. |
| 04-database/1-1-decisions-from-survey.md | 10 | Nội dung / Quyết định |
| 04-database/1-2-conventions.md | 12 | Tên bảng, cột: tiếng Anh, snake_case, bảng số nhiều. |
| 04-database/2-erd-schema-core.md | 210 | 21 bảng, do core-api sở hữu. |
| 04-database/3-erd-schema-ai.md | 117 | 11 bảng, do ai-service sở hữu. |
| 04-database/4-data-dictionary-schema-core.md | 5 | Cột id uuid PK và created_at timestamptz NOT NULL DEFAULT now() không nhắc lại ở từng bảng. |
| 04-database/users.md | 16 | Cột / Kiểu / Ràng buộc / Ý nghĩa |
| 04-database/auth-tokens.md | 13 | Cột / Kiểu / Ràng buộc / Ý nghĩa |
| 04-database/provinces-wards.md | 14 | Bảng.cột / Kiểu / Ràng buộc / Ý nghĩa |
| 04-database/addresses.md | 12 | Cột / Kiểu / Ràng buộc / Ý nghĩa |
| 04-database/categories-size-charts.md | 11 | Bảng.cột / Kiểu / Ràng buộc / Ý nghĩa |
| 04-database/products.md | 18 | Cột / Kiểu / Ràng buộc / Ý nghĩa |
| 04-database/product-variants.md | 15 | Cột / Kiểu / Ràng buộc / Ý nghĩa |
| 04-database/product-images.md | 13 | Cột / Kiểu / Ràng buộc / Ý nghĩa |
| 04-database/promotions.md | 9 | Cột / Kiểu / Ràng buộc / Ý nghĩa |
| 04-database/cart-items.md | 11 | Cột / Kiểu / Ràng buộc / Ý nghĩa |
| 04-database/orders.md | 20 | Cột / Kiểu / Ràng buộc / Ý nghĩa |
| 04-database/order-items.md | 12 | Cột / Kiểu / Ràng buộc / Ý nghĩa |
| 04-database/order-status-history.md | 10 | Cột / Kiểu / Ràng buộc / Ý nghĩa |
| 04-database/payments.md | 17 | Cột / Kiểu / Ràng buộc / Ý nghĩa |
| 04-database/inventory-ledger.md | 12 | Cột / Kiểu / Ràng buộc / Ý nghĩa |
| 04-database/reviews.md | 10 | Cột / Kiểu / Ràng buộc / Ý nghĩa |
| 04-database/faqs.md | 13 | Cột / Kiểu / Ràng buộc / Ý nghĩa |
| 04-database/settings-setting-history.md | 13 | Bảng.cột / Kiểu / Ràng buộc / Ý nghĩa |
| 04-database/5-data-dictionary-schema-ai.md | 5 | Quy ước như mục 4. |
| 04-database/photo-consents.md | 11 | Cột / Kiểu / Ràng buộc / Ý nghĩa |
| 04-database/user-photos.md | 11 | Cột / Kiểu / Ràng buộc / Ý nghĩa |
| 04-database/tryon-jobs.md | 19 | Cột / Kiểu / Ràng buộc / Ý nghĩa |
| 04-database/tryon-job-items.md | 10 | Cột / Kiểu / Ràng buộc / Ý nghĩa |
| 04-database/webcam-sessions.md | 16 | Cột / Kiểu / Ràng buộc / Ý nghĩa |
| 04-database/conversations.md | 11 | Cột / Kiểu / Ràng buộc / Ý nghĩa |
| 04-database/chat-messages.md | 14 | Cột / Kiểu / Ràng buộc / Ý nghĩa |
| 04-database/pending-actions.md | 12 | Cột / Kiểu / Ràng buộc / Ý nghĩa |
| 04-database/outfit-suggestions.md | 9 | Cột / Kiểu / Ràng buộc / Ý nghĩa |
| 04-database/search-documents.md | 14 | Cột / Kiểu / Ràng buộc / Ý nghĩa |
| 04-database/ai-cost-records.md | 15 | Cột / Kiểu / Ràng buộc / Ý nghĩa |
| 04-database/6-3nf-check-and-intentional-exceptions.md | 3 |  |
| 04-database/6-1-check-per-normal-form.md | 9 | Dạng chuẩn / Điều kiện / Cách đáp ứng |
| 04-database/6-2-intentional-exceptions.md | 15 | Chỗ / Vì sao vẫn lưu / Cách giữ đúng |
| 04-database/7-changes-from-b2-entities.md | 32 | B2 có 32 entity; B4 có 32 bảng nhưng không tương ứng một–một. |
| 04-database/8-index-delete-rules-seed-data.md | 3 |  |
| 04-database/8-1-index.md | 30 | PK và UNIQUE đã có index. |
| 04-database/8-2-delete-rules.md | 10 | Không xóa cứng users, orders, payments, inventory_ledger: tài khoản thì khóa (status), đơn thì hủy (status). |
| 04-database/8-3-seed-data.md | 13 | Dữ liệu / Bảng / Nguồn |
| 05-api-contract-events/_overview.md | 7 | Nov 3, 2026 · @Ly |
| 05-api-contract-events/1-general-conventions.md | 5 | B5 đặc tả giao tiếp giữa web, core-api, ai-service, worker và hệ thống ngoài theo các interface ở B3 mục 4, dùng bảng… |
| 05-api-contract-events/1-1-addresses.md | 13 | API / Địa chỉ / Ai gọi |
| 05-api-contract-events/1-2-data-formats.md | 13 | Nội dung / Quy ước |
| 05-api-contract-events/1-3-pagination-filter-sort.md | 7 | Danh sách dùng ?page=1&page_size=20 (page_size tối đa 100). |
| 05-api-contract-events/1-4-errors.md | 30 | Mọi lỗi trả application/problem+json (RFC 9457) cộng trường code để web hiển thị thông báo theo ngôn ngữ; detail chỉ… |
| 05-api-contract-events/1-5-idempotency-and-rate-limiting.md | 8 | POST /orders và các POST tạo job thử đồ nhận header Idempotency-Key (UUID do web sinh mỗi lần bấm). |
| 05-api-contract-events/2-authentication-and-authorization.md | 3 |  |
| 05-api-contract-events/2-1-access-and-refresh-tokens.md | 16 | Token / Nơi giữ / Gửi thế nào / Hạn |
| 05-api-contract-events/2-2-jwt-claims.md | 15 | Claim / Giá trị |
| 05-api-contract-events/2-3-guest.md | 9 | Trường hợp / Cách nhận diện |
| 05-api-contract-events/2-4-agent-tools-calling-core-br17.md | 8 | Mỗi request chat hoặc xác nhận hành động đều kèm access token hiện tại của người dùng. |
| 05-api-contract-events/2-5-internal-and-webhook.md | 9 | Kênh / Xác thực |
| 05-api-contract-events/2-6-permission-notation-in-endpoint-tables.md | 14 | Ký hiệu / Ai được gọi |
| 05-api-contract-events/3-core-api-endpoints.md | 5 | Đường dẫn tính từ /api/v1. |
| 05-api-contract-events/3-1-authentication-and-accounts-identity.md | 22 | Method / Path / Quyền / UC / Ghi chú |
| 05-api-contract-events/3-2-products-cart-orders-customer-side.md | 23 | Method / Path / Quyền / UC / Chi tiết / Ghi chú |
| 05-api-contract-events/3-3-operations-staff.md | 26 | Method / Path / Quyền / UC / Ghi chú |
| 05-api-contract-events/3-4-administration-admin.md | 23 | Method / Path / Quyền / UC / Ghi chú |
| 05-api-contract-events/4-ai-service-and-internal-endpoints.md | 3 |  |
| 05-api-contract-events/4-1-ai-service-public-ai-v1.md | 31 | Method / Path / Quyền / UC / Chi tiết / Ghi chú |
| 05-api-contract-events/4-2-core-api-internal-internal-v1-service.md | 11 | Method / Path / Người gọi / Dùng cho |
| 05-api-contract-events/4-3-ai-service-internal-internal-v1-service.md | 7 | Method / Path / Người gọi / Dùng cho |
| 05-api-contract-events/5-contracts-of-main-flows.md | 5 | Schema đầy đủ nằm trong file mirra-openapi.yaml (OpenAPI 3.1, 18 path, đã kiểm hợp lệ). |
| 05-api-contract-events/5-1-order-and-vietqr-payment-uc07-uc08.md | 39 | Web gọi POST /api/v1/checkout/quote mỗi khi đổi địa chỉ hoặc giỏ. |
| 05-api-contract-events/5-2-assistant-chat-and-action-confirmation-uc15-uc16-uc31.md | 51 | Guest xin POST /ai/v1/chat/guest-sessions một lần; người đã đăng nhập dùng access token. |
| 05-api-contract-events/5-3-photo-set-and-video-try-on-uc12-uc13-uc14-uc32.md | 32 | Lần đầu: GET /ai/v1/tryon/consent, chưa đồng ý thì hiện hộp thoại rồi POST /tryon/consent. |
| 05-api-contract-events/5-4-webcam-try-on-uc33.md | 20 | Trang sản phẩm và thẻ trong chat gọi GET /ai/v1/webcam/availability để hiện hoặc ẩn nút. |
| 05-api-contract-events/6-events.md | 3 |  |
| 05-api-contract-events/6-1-sse-to-browser.md | 11 | Endpoint / Sự kiện / Đóng khi / Kết nối lại |
| 05-api-contract-events/6-2-redis-streams.md | 24 | Mọi thông điệp có hai trường Redis: type và data (chuỗi JSON). |
| 05-api-contract-events/6-3-redis-pub-sub.md | 10 | Kênh / Bên phát / Bên nghe / Nội dung |
| 05-api-contract-events/6-4-opentelemetry-and-langfuse.md | 6 | Mọi request mang header traceparent (W3C); web tạo ở trình duyệt, core và ai truyền tiếp khi gọi nhau và ghi vào data… |
| 05-api-contract-events/7-error-codes-and-config-keys.md | 3 |  |
| 05-api-contract-events/7-1-error-codes.md | 51 | Nhóm / Code / HTTP |
| 05-api-contract-events/7-2-config-keys-settings-uc27.md | 33 | B4 để lại tên khóa và kiểu giá trị cho B5. |
| 05-api-contract-events/8-openapi-file-and-points-to-verify.md | 3 |  |
| 05-api-contract-events/8-1-attached-files.md | 8 | mirra-openapi.yaml (OpenAPI 3.1.0, gửi kèm trong đoạn chat) gồm 18 path của các endpoint đánh dấu ✓ ở mục 3, 4 và 20… |
| 05-api-contract-events/8-2-changes-from-b3-b4.md | 9 | Chỗ / Thay đổi / Lý do |
| 05-api-contract-events/8-3-to-verify-when-coding.md | 9 | Điểm / Kiểm bằng |
| 06-class-and-design-pattern/_overview.md | 7 | Nov 4, 2026 · @Ly |
| 06-class-and-design-pattern/1-conventions-and-decisions.md | 5 | B6 đi từ package và component ở B3 xuống mức lớp: mỗi lớp có trách nhiệm gì, phụ thuộc vào đâu, các luồng chính chạy… |
| 06-class-and-design-pattern/1-1-decisions-from-survey.md | 10 | Nội dung / Quyết định |
| 06-class-and-design-pattern/1-2-notation.md | 9 | Sơ đồ lớp bằng Mermaid classDiagram, bạn vẽ lại UML chuẩn trong Astah. |
| 06-class-and-design-pattern/1-3-design-rules.md | 9 | Service nhận phụ thuộc qua constructor (FastAPI Depends lắp ráp), không tự tạo adapter hay session. |
| 06-class-and-design-pattern/2-shared-base-classes.md | 99 | Cả core-api và ai-service đều có các lớp nền dưới đây trong package core của mình (mỗi service một bản, không chia sẻ… |
| 06-class-and-design-pattern/3-core-api.md | 5 | Router (tầng api) không vẽ: mỗi router chỉ kiểm DTO của B5, lấy CurrentUser và gọi một method service. |
| 06-class-and-design-pattern/3-1-identity-uc01-uc04-uc24-uc25.md | 105 | classDiagram |
| 06-class-and-design-pattern/3-2-catalog-uc05-uc11-uc17-uc21-uc22.md | 102 | classDiagram |
| 06-class-and-design-pattern/3-3-ordering-uc06-uc10-uc19-uc20-uc23-uc29.md | 172 | classDiagram |
| 06-class-and-design-pattern/3-4-administration-uc26-uc27.md | 65 | classDiagram |
| 06-class-and-design-pattern/3-5-core-worker.md | 50 | classDiagram |
| 06-class-and-design-pattern/4-ai-service.md | 3 |  |
| 06-class-and-design-pattern/4-1-assistant-uc15-uc16-uc31.md | 162 | classDiagram |
| 06-class-and-design-pattern/4-2-tryon-uc12-uc14-uc30-uc32-and-ai-worker.md | 122 | classDiagram |
| 06-class-and-design-pattern/4-3-webcam-uc33.md | 72 | classDiagram |
| 06-class-and-design-pattern/4-4-knowledge-semantic-search-uc18.md | 57 | classDiagram |
| 06-class-and-design-pattern/4-5-observability-uc26-uc28.md | 71 | classDiagram |
| 06-class-and-design-pattern/5-design-level-sequences.md | 5 | Khác B2: participant là lớp thật ở mục 3, 4; thể hiện ranh giới transaction và việc gọi ra ngoài sau commit. |
| 06-class-and-design-pattern/5-1-place-order-uc07.md | 53 | sequenceDiagram |
| 06-class-and-design-pattern/5-2-payos-webhook-uc08.md | 49 | sequenceDiagram |
| 06-class-and-design-pattern/5-3-chat-and-action-confirmation-uc15-uc16.md | 56 | sequenceDiagram |
| 06-class-and-design-pattern/5-4-set-try-on-via-job-uc32-uc12-same-without-compositing.md | 50 | sequenceDiagram |
| 06-class-and-design-pattern/5-5-open-and-close-webcam-session-uc33.md | 41 | sequenceDiagram |
| 06-class-and-design-pattern/6-design-patterns.md | 13 | Pattern / Áp dụng ở / Vấn đề giải quyết |
| 06-class-and-design-pattern/6-1-adapter-and-strategy.md | 33 | classDiagram |
| 06-class-and-design-pattern/6-2-state-why-use-a-table.md | 7 | GoF nêu State có thể cài bằng mỗi trạng thái một lớp, hoặc bằng bảng ánh xạ (trạng thái, sự kiện) → trạng thái mới. |
| 06-class-and-design-pattern/6-3-template-method.md | 30 | classDiagram |
| 06-class-and-design-pattern/6-4-observer.md | 11 | Ba mức, cùng ý: bên phát không phụ thuộc bên nhận. |
| 06-class-and-design-pattern/6-5-repository-unit-of-work-factory.md | 7 | Repository trả model ORM, nhận tham số nghiệp vụ (find_cached, find_expired_unpaid), không lộ câu SQL ra service. |
| 06-class-and-design-pattern/7-coupling-and-cohesion.md | 3 |  |
| 06-class-and-design-pattern/7-1-assessment-per-component.md | 17 | Component / Cohesion / Phụ thuộc ra ngoài component / Kiểu coupling |
| 06-class-and-design-pattern/7-2-accepted-exceptions.md | 14 | Ngoại lệ / Lý do / Giới hạn |
| 06-class-and-design-pattern/7-3-how-to-stay-compliant-when-coding.md | 7 | import-linter chạy trong CI với các contract: tầng api → services → domain/repositories → models (không import ngược)… |
| 06-class-and-design-pattern/8-changes-from-b2-b5.md | 25 | Chỗ / B6 / Lý do |
| 07-ai-agent/_overview.md | 7 | Nov 8, 2026 · @Ly |
| 07-ai-agent/1-scope-and-conventions.md | 18 | B7 thiết kế bên trong trợ lý AI: state, graph, tool, prompt, guardrail và cách đánh giá. |
| 07-ai-agent/2-agent-state.md | 5 | State là dữ liệu graph mang theo qua từng bước. |
| 07-ai-agent/2-1-decisions-agreed-nov-08.md | 13 | Vấn đề / Chốt / Lý do ngắn |
| 07-ai-agent/2-2-where-data-lives.md | 17 | Có ba chỗ giữ dữ liệu của một hội thoại. |
| 07-ai-agent/2-3-schema.md | 44 | from dataclasses import dataclass |
| 07-ai-agent/2-4-history-window-sent-to-llm.md | 30 | Token phình lên chủ yếu vì kết quả tool: một lần tìm sản phẩm trả về khoảng 10 món, tức 2–3k token nếu để nguyên. |
| 07-ai-agent/2-5-product-cards-and-set-cards.md | 9 | Tool đặt dữ liệu thẻ vào ToolMessage.artifact. |
| 07-ai-agent/2-6-pending-confirmation-actions.md | 24 | stateDiagram-v2 |
| 07-ai-agent/2-7-five-tool-calls-per-turn-limit.md | 8 | Node agent đếm số ToolMessage kể từ HumanMessage cuối cùng. |
| 07-ai-agent/2-8-checkpoint-size.md | 14 | Mỗi khi messages đổi, checkpointer Postgres lưu một phiên bản mới của cả danh sách, nên dung lượng của một hội thoại… |
| 07-ai-agent/3-graph.md | 3 |  |
| 07-ai-agent/3-1-decisions-agreed-nov-08.md | 10 | Vấn đề / Chốt / Lý do ngắn |
| 07-ai-agent/3-2-graph-diagram.md | 39 | flowchart TD |
| 07-ai-agent/3-3-confirm-node-and-rerun-on-resume-trap.md | 28 | Khi resume sau interrupt, LangGraph chạy lại node confirm từ đầu, không phải từ dòng interrupt. |
| 07-ai-agent/3-4-one-chat-turn-seen-from-agentrunner.md | 51 | Sơ đồ này thay sequence "Chat và xác nhận" ở B6 mục 5.3 cho phần gửi tin; phần bấm xác nhận giữ nguyên như B6. |
| 07-ai-agent/3-5-errors-and-limits.md | 11 | Tình huống / Xử lý |
| 07-ai-agent/3-6-thread-lifecycle-and-checkpoint-cleanup.md | 13 | thread_id = conversations.id, như B6. |
| 07-ai-agent/4-tools.md | 3 |  |
| 07-ai-agent/4-1-decisions-agreed-nov-08.md | 10 | Vấn đề / Chốt |
| 07-ai-agent/4-2-tool-list-by-role.md | 27 | Tool / Guest / Customer / Staff / Admin / Ghi? |
| 07-ai-agent/4-3-general-conventions.md | 60 | Tham số dùng slug, màu, size, mã đơn 10 số; không dùng UUID. |
| 07-ai-agent/4-4-each-tool.md | 37 | Tool / Tham số / Xử lý / content trả cho LLM |
| 07-ai-agent/4-5-search-products-vector-search-then-filter-in-core.md | 13 | Có query: embed câu tìm bằng EmbeddingProvider, lấy 30 sản phẩm gần nhất trong search_documents (chỉ source_type = pr… |
| 07-ai-agent/4-6-two-write-tools.md | 17 | add_to_cart (BR05, BR17): |
| 07-ai-agent/5-prompts.md | 3 |  |
| 07-ai-agent/5-1-decisions-agreed-nov-08.md | 13 | Vấn đề / Chốt |
| 07-ai-agent/5-2-system-prompt-structure.md | 18 | PromptBuilder ghép system prompt ở mỗi lượt theo thứ tự cố định. |
| 07-ai-agent/5-3-base-md.md | 33 | You are Mirra Assistant, the shopping assistant of Mirra, an online women's fashion store in Vietnam. |
| 07-ai-agent/5-4-role-specific-parts.md | 41 | <!-- role_guest.md --> |
| 07-ai-agent/5-5-tool-descriptions-for-model.md | 12 | Mỗi tool có một description tiếng Anh gồm ba ý: tool làm gì, khi nào dùng, khi nào không dùng. |
| 07-ai-agent/5-6-classifier-model-prompt-layer-1-step-c1.md | 15 | You classify one message sent to the shopping assistant of an online fashion store. |
| 07-ai-agent/5-7-storage-and-versioning.md | 19 | ai_service/agent/prompts/ |
| 07-ai-agent/6-guardrails.md | 3 |  |
| 07-ai-agent/6-1-decisions-agreed-nov-08.md | 10 | Vấn đề / Chốt |
| 07-ai-agent/6-2-four-layers.md | 14 | Nguyên tắc: thứ gì quan trọng thì chặn bằng code, không trông vào việc LLM làm theo hướng dẫn. |
| 07-ai-agent/6-3-layer-1-input.md | 24 | Chạy theo thứ tự; bước nào chặn thì dừng ở đó. |
| 07-ai-agent/6-4-layer-2-context.md | 22 | Những gì được đưa vào ngữ cảnh của model: |
| 07-ai-agent/6-5-layer-3-output.md | 19 | Khi agent trả lời xong, Guardrail.check_output(text, tool_data) kiểm ba điều. |
| 07-ai-agent/6-6-layers-in-code.md | 11 | Guardrail của B6 được tách thành ba phần nhỏ, mỗi phần kiểm thử riêng: |
| 07-ai-agent/7-agent-evaluation-plan.md | 3 |  |
| 07-ai-agent/7-1-decisions-agreed-nov-08.md | 12 | Vấn đề / Chốt |
| 07-ai-agent/7-2-what-to-measure.md | 16 | Chỉ số / Cách tính / Nguồn yêu cầu |
| 07-ai-agent/7-3-test-case-structure.md | 29 | Mỗi ca là một dòng JSONL. |
| 07-ai-agent/7-4-coverage-matrix.md | 26 | Tỉ lệ gợi ý cho mỗi vai trò. |
| 07-ai-agent/7-5-test-case-generation-rules.md | 40 | Dữ liệu |
| 07-ai-agent/7-6-scoring.md | 7 | Kiểm bằng code (mỗi ca, mỗi trường expect): chuỗi tool, tham số, must_not_tools, blocked, interrupt, ngôn ngữ trả lời. |
| 07-ai-agent/7-7-environment-how-to-run-thresholds.md | 22 | FakeCoreApiClient cài cùng interface CoreApiClient (B6), trả dữ liệu từ fixture: khoảng 20 sản phẩm, vài người dùng g… |
| 07-ai-agent/8-changes-from-b4-b6.md | 15 | Cả 8 mục của B7 đã được duyệt ngày 08/11. |
| 08-ui-design/_overview.md | 9 | Nov 10, 2026 · @Ly |
| 08-ui-design/ui-standardization.md | 44 | Mọi giá trị dưới đây lấy từ Design System Mirra (token) để mọi màn dùng thống nhất. |
| 08-ui-design/component-library.md | 17 | Toàn bộ token và component nằm trong [Design System Mirra](https://claude.ai/artifact/9b6hjNcuM5S8zNuxjJwZ1h) — xem t… |
| 08-ui-design/screen-list.md | 72 | 44 artboard: 26 màn cửa hàng, 12 màn Staff/Admin, 6 bản mobile. |
| 08-ui-design/screen-flow-diagram.md | 7 | Cột trái là luồng mua hàng chính của Guest/Customer; cột phải là Mirra AI, mở được từ mọi trang và đổ lại vào giỏ hàng. |
| 08-ui-design/main-screen-specs.md | 69 | Đặc tả các màn trọng tâm: thành phần chính, thao tác và trạng thái. |
| 08-ui-design/differences-from-rechic-template.md | 12 | Mirra bám bố cục, cấu trúc trang và phong cách của Rechic, nhưng điều chỉnh theo phạm vi đã chốt và tính năng riêng: |
| 08-ui-design/mockup-links.md | 8 | Toàn bộ 44 artboard nằm trên canvas [Mirra B8 Mockups](https://claude.ai/artifact/JcW5sBZNfPepKtmZzRZwhU), chia theo… |
| 09-testing/_overview.md | 9 | Nov 11, 2026 · @Ly |
| 09-testing/test-strategy-and-levels.md | 17 | Kiểm thử theo kim tự tháp: nhiều unit test ở đáy, ít E2E ở đỉnh. |
| 09-testing/test-case-design-techniques.md | 37 | Dùng ba kỹ thuật, mỗi kỹ thuật hợp với một loại logic khác nhau. |
| 09-testing/sample-test-case-table.md | 78 | Tám luồng đại diện, phủ mọi nhóm chức năng và cả ba kỹ thuật trên; mỗi luồng có ít nhất một ca âm. |
| 09-testing/test-code-skeleton.md | 50 | Mỗi service có thư mục test riêng, chia theo mức. |
| 09-testing/ai-agent-evaluation-and-tryon-benchmark.md | 36 | Đánh giá AI agent là một nhánh test riêng, chi tiết ở [B7](https://claude.ai/artifact/JqesBMTsjrfCLztNEuy1sk) mục 7;… |
| 09-testing/non-functional-testing.md | 28 | Load test (k6). |
| 09-testing/environment-data-and-exit-criteria.md | 27 | Môi trường test. |

## 3. Cách dùng

Đọc INDEX trước, chỉ mở file cần thiết, không đọc cả thư mục.
