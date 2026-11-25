Nguồn: 03-PACKAGE-COMPONENT-DEPLOYMENT.md > Mirra — B3: Package, Component, Deployment > 2. Sơ đồ package > 2.4 web
### 2.4 web

```mermaid
flowchart TB
  subgraph web["«package» web"]
    direction TB
    AUTH["app/(auth)<br/>login, register, verify-email, reset-password"]
    SHOP["app/(shop)<br/>products, product detail, cart, checkout, payment,<br/>orders, account, tryon, tryon history, webcam"]
    ADMIN["app/(admin)/admin<br/>products, inventory, orders, faq, pricing, refunds,<br/>customers, staff, reports, settings, traces"]
    MW["middleware<br/>session check, role guard for /admin"]
    CMP["components<br/>ui (shadcn), shop, admin, chat, tryon"]
    ST["stores<br/>Zustand: guest cart, chat UI"]
    LIB["lib<br/>coreApi, aiApi (TanStack Query), auth refresh,<br/>sse client, webrtc client, zod schemas"]
    I18N["i18n<br/>next-intl messages"]
  end
  MW --> AUTH
  MW --> SHOP
  MW --> ADMIN
  AUTH --> CMP
  SHOP --> CMP
  ADMIN --> CMP
  CMP --> ST
  CMP --> LIB
  ST --> LIB
  CMP -.-> I18N
```

- Nhóm route `(auth)`, `(shop)`, `(admin)` tách layout; `middleware` chặn `/admin` với vai trò không phải Staff/Admin (API vẫn kiểm tra lại, không tin client).
- `lib.coreApi` và `lib.aiApi` là hai client riêng, cùng cơ chế gắn access token và làm mới token; `sse client` dùng cho chat, tiến trình try-on, trạng thái thanh toán; `webrtc client` dùng cho UC33.
- Giỏ hàng của Guest nằm trong `stores` (lưu ở trình duyệt), gộp vào giỏ server khi đăng nhập (UC06.3).

