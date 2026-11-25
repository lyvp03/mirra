Nguồn: 03-PACKAGE-COMPONENT-DEPLOYMENT.md > Mirra — B3: Package, Component, Deployment > 3. Ánh xạ lớp B2 vào package > 3.2 Control dùng chung
### 3.2 Control dùng chung

| Control B2 | Service | Package |
| --- | --- | --- |
| StockPolicy, ShippingFeeCalculator, OrderStateMachine | core\_api | `domain` |
| ImageValidator | cả hai | tách đôi: `core_api.domain.FileValidator` (định dạng, ≤ 5 MB) và `ai_service.domain.ImageValidator` (thêm kiểm tra ảnh người qua `PersonDetector`) |
| TryOnQuotaPolicy, OutfitComposer | ai\_service | `domain` |
| Guardrail, ToolRegistry, AccessPolicy | ai\_service | `agent` |
| BusinessControllers (đại diện ở UC15) | core\_api | REST API của core, được tool gọi qua `CoreApiClient` |

