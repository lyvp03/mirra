Nguồn: 03-PACKAGE-COMPONENT-DEPLOYMENT.md > Mirra — B3: Package, Component, Deployment > 3. Ánh xạ lớp B2 vào package > 3.3 Boundary hệ thống ngoài
### 3.3 Boundary hệ thống ngoài

| Boundary B2 | Service | Interface → adapter |
| --- | --- | --- |
| PaymentGatewayBoundary | core\_api | `PaymentGateway` → `PayOSAdapter` |
| EmailServiceBoundary | core\_api | `EmailSender` → `SmtpEmailAdapter`; core\_api xếp hàng, core\_worker gửi |
| TryOnServiceBoundary | ai\_service | `TryOnProvider` → adapter theo provider chọn sau benchmark |
| RealtimeTryOnBoundary | ai\_service | `RealtimeTryOnProvider` → adapter theo provider chọn sau benchmark |
| LLMBoundary | ai\_service | `LLMProvider` → adapter bọc chat model của LangChain |
| EmbeddingBoundary | ai\_service | `EmbeddingProvider` → adapter embedding |
| TraceStoreBoundary | ai\_service | `TraceStore` → `LangfuseAdapter` |
| SchedulerBoundary | core\_worker, ai\_worker | APScheduler trong `workers` |

