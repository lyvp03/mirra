Nguồn: 03-PACKAGE-COMPONENT-DEPLOYMENT.md > Mirra — B3: Package, Component, Deployment > 4. Sơ đồ component > 4.1 Các component của hệ thống
### 4.1 Các component của hệ thống

```mermaid
flowchart LR
  BR["«component» Browser client<br/>web bundle, SSE, WebRTC"]
  CAD["«component» Caddy<br/>TLS, path routing"]
  WEB["«component» web<br/>Next.js SSR"]
  CORE["«component» core_api<br/>provides ICoreRest, IJwks,<br/>ICoreInternal, IPaymentWebhook"]
  AI["«component» ai_service<br/>provides IAiRest, IAiInternal,<br/>ITryOnCallback"]
  RD[("Redis<br/>IEventStream, IJobQueue")]
  CW["«component» core_worker"]
  AW["«component» ai_worker"]
  BR -->|HTTPS| CAD
  CAD -->|"/"| WEB
  CAD -->|"/api: ICoreRest"| CORE
  CAD -->|"/ai: IAiRest"| AI
  WEB -->|"ICoreRest (SSR)"| CORE
  AI -->|"ICoreRest with user JWT,<br/>IJwks, ICoreInternal"| CORE
  CORE -->|"IAiInternal (reports)"| AI
  CORE -->|"events, email jobs"| RD
  AI -->|"try-on jobs"| RD
  RD -->|consume| CW
  RD -->|consume| AW
  AW -->|"ICoreInternal"| CORE
```

PostgreSQL và MinIO không vẽ ở đây để sơ đồ gọn; mỗi service và worker truy cập schema và bucket của mình như mục 3.5, xem thêm mục 5. Trình duyệt tải ảnh qua URL ký sẵn của MinIO và nối WebRTC thẳng tới dịch vụ realtime, không đi qua service.

