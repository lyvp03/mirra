Nguồn: 03-PACKAGE-COMPONENT-DEPLOYMENT.md > Mirra — B3: Package, Component, Deployment > 2. Sơ đồ package > 2.1 Package cấp service
### 2.1 Package cấp service

Bốn package ứng với bốn đơn vị triển khai. Hai worker dùng chung code với service tương ứng (phụ thuộc `import`), chỉ khác lệnh khởi động. Mũi tên liền là gọi qua mạng, nét đứt là phụ thuộc mã hoặc sự kiện bất đồng bộ.

```mermaid
flowchart LR
  WEB["«package» web<br/>Next.js pages, components, API clients"]
  CORE["«package» core_api<br/>accounts, catalog, cart, orders,<br/>payments, inventory, admin"]
  AI["«package» ai_service<br/>agent, try-on, webcam,<br/>outfits, search index"]
  CW["«package» core_worker<br/>scheduled jobs, email sending"]
  AW["«package» ai_worker<br/>try-on jobs, index sync,<br/>photo retention, webcam sweep,<br/>checkpoint cleanup"]
  WEB -->|REST| CORE
  WEB -->|REST, SSE| AI
  AI -->|"REST with user JWT, /internal"| CORE
  CORE -->|"/internal usage"| AI
  CW -.->|import| CORE
  AW -.->|import| AI
  CORE -.->|"Redis Streams events"| AW
```

