Nguồn: 03-PACKAGE-COMPONENT-DEPLOYMENT.md > Mirra — B3: Package, Component, Deployment > 5. Sơ đồ deployment > 5.2 Container
### 5.2 Container

| Container | Image | Vai trò | Mạng | Cổng | Volume |
| --- | --- | --- | --- | --- | --- |
| caddy | `caddy:2` | TLS tự động; định tuyến `/` → web, `/api` → core-api, `/ai` → ai-service, tên miền phụ media → minio; tắt buffer cho SSE | edge | 80, 443 công khai | caddy\_data, caddy\_config |
| web | `mirra/web` (Node 24, Next.js standalone) | SSR, tài nguyên tĩnh | edge | 3000 | — |
| core-api | `mirra/core` (Python 3.12, uv) | ICoreRest, IJwks, ICoreInternal, webhook payOS, SSE thanh toán | edge, backend | 8000 | — |
| core-worker | `mirra/core`, lệnh worker | APScheduler (UC29), đọc hàng email | backend | — | — |
| ai-service | `mirra/ai` (Python 3.12, uv) | IAiRest, IAiInternal, webhook try-on, SSE chat và tiến trình | edge, backend | 8001 | — |
| ai-worker | `mirra/ai`, lệnh worker | Job try-on, đồng bộ chỉ mục, xóa ảnh 30 ngày (UC30), dọn phiên webcam | backend | — | — |
| postgres | `pgvector/pgvector:pg17` | Schema `core`, `ai`; 2 DB user, mỗi user chỉ có quyền trên schema của mình | backend | 5432 | pg\_data |
| redis | `redis:7-alpine`, bật AOF | Streams, pub/sub, cache, giới hạn tần suất | backend | 6379 | redis\_data |
| minio | `minio/minio` | Bucket `products` (đọc công khai), `tryon` (riêng tư, URL ký ngắn hạn) | edge, backend | 9000 (console không mở) | minio\_data |
| jaeger | Jaeger all-in-one | Nhận trace OpenTelemetry, giao diện xem trace | backend | 4317, 16686 (chỉ qua SSH tunnel) | Không; trace lưu trong bộ nhớ |

Hai mạng Docker: `edge` nối Caddy với các container nó định tuyến tới; `backend` nối service, worker với dữ liệu và Jaeger. Postgres, Redis, Jaeger không nằm trên `edge` nên Caddy không chạm tới được. Container vẫn gọi ra Internet được (payOS, provider, Langfuse).

