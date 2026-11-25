Nguồn: 03-PACKAGE-COMPONENT-DEPLOYMENT.md > Mirra — B3: Package, Component, Deployment > 2. Sơ đồ package > 2.2 core\_api
### 2.2 core\_api

```mermaid
flowchart TB
  subgraph core_api["«package» core_api"]
    direction TB
    API["api<br/>routers: auth, account, catalog, cart, orders,<br/>payments, inventory, reviews, faq, admin, internal"]
    SCH["schemas<br/>Pydantic request/response DTOs"]
    SVC["services<br/>AuthService, ProfileService, CatalogService, CartService,<br/>OrderService, PaymentService, InventoryService, ReviewService,<br/>FaqService, PricingService, AccountAdminService,<br/>ReportService, SettingsService"]
    DOM["domain<br/>StockPolicy, ShippingFeeCalculator,<br/>OrderStateMachine, FileValidator"]
    REP["repositories<br/>one repository per aggregate"]
    MOD["models<br/>SQLAlchemy, schema core"]
    ADP["adapters<br/>PaymentGateway, EmailSender, EventPublisher,<br/>ObjectStorage, AiServiceClient"]
    WRK["workers<br/>OrderExpiryJob, EmailConsumer"]
    CFG["core<br/>config, JWT signing and JWKS, db session,<br/>rate limit, telemetry"]
  end
  API --> SCH
  API --> SVC
  WRK --> SVC
  SVC --> DOM
  SVC --> REP
  SVC --> ADP
  REP --> MOD
  API -.-> CFG
  SVC -.-> CFG
  REP -.-> CFG
```

- `api` chỉ kiểm tra đầu vào, lấy người dùng từ JWT và gọi `services`; không chứa nghiệp vụ.
- `services` giữ transaction: một lời gọi service là một đơn vị công việc (ví dụ đặt hàng gồm giữ chỗ kho, tạo đơn, tạo thanh toán trong một transaction).
- `adapters.EventPublisher` ghi sự kiện ra Redis Streams sau khi transaction commit; `AiServiceClient` chỉ dùng cho báo cáo (UC26) lấy số liệu AI qua `/internal`.
- `FileValidator` là phần kiểm tra định dạng, dung lượng của `ImageValidator` ở B2 dùng cho ảnh sản phẩm; phần kiểm tra ảnh người nằm ở ai\_service.

