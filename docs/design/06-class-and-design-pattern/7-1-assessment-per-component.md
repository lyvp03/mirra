Nguồn: 06-CLASS-AND-DESIGN-PATTERN.md > Mirra — B6: Thiết kế lớp và design pattern > 7. Coupling và cohesion > 7.1 Đánh giá theo component
### 7.1 Đánh giá theo component

| Component | Cohesion | Phụ thuộc ra ngoài component | Kiểu coupling |
| --- | --- | --- | --- |
| Identity | Chức năng: mọi lớp phục vụ danh tính và tài khoản | `EmailQueue`, Redis (`LoginThrottle`) | Dữ liệu qua interface |
| Catalog | Chức năng: sản phẩm, giá, đánh giá, FAQ | `ObjectStorage`, `EventPublisher`; bảng `orders`, `order_items` (chỉ đọc, xác minh đánh giá) | Dữ liệu qua interface; ngoại lệ đọc (7.2) |
| Ordering | Chức năng: giỏ, đơn, thanh toán, kho | `PricingService`, `VariantRepository` (Catalog), `PaymentGateway`, `EmailQueue`, `Notifier` | Dữ liệu; một ngoại lệ dùng chung repository (7.2) |
| Administration | Truyền thông tin (communicational): cùng thao tác trên số liệu tổng hợp và cấu hình | `OrderRepository` (chỉ đọc), `AiUsageClient`, `EventPublisher` | Dữ liệu; ngoại lệ đọc báo cáo (7.2) |
| Assistant | Chức năng: hội thoại và agent | `CoreApiClient`, `LLMProvider`, `TraceStore`, `SearchIndexService` | Dữ liệu qua interface và service |
| TryOn | Chức năng: thử đồ bằng ảnh | `CoreApiClient`, `TryOnProvider`, `ObjectStorage`, `JobQueue`, `CostRecorder` | Dữ liệu qua interface |
| Webcam | Chức năng: phiên webcam và ngân sách | `RealtimeTryOnProvider`, `OutfitComposer`, `SetRule` (TryOn), `TryOnJobRepository` (ghi khung hình), `CostRecorder` | Dữ liệu; dùng chung domain với TryOn |
| Knowledge | Chức năng: chỉ mục và nháp sản phẩm | `CoreApiClient`, `EmbeddingProvider`, `LLMProvider`, `CostRecorder` | Dữ liệu qua interface |
| Observability | Truyền thông tin: cùng đọc dữ liệu hoạt động AI | Repository của TryOn, Webcam, Assistant (chỉ đếm), `TraceStore` | Dữ liệu; ngoại lệ đọc báo cáo (7.2) |

Không component nào dùng control coupling (truyền cờ điều khiển luồng của bên kia) hay common coupling (biến toàn cục); cấu hình đi qua `SettingsProvider` được inject.

