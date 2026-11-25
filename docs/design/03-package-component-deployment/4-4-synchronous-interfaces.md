Nguồn: 03-PACKAGE-COMPONENT-DEPLOYMENT.md > Mirra — B3: Package, Component, Deployment > 4. Sơ đồ component > 4.4 Interface đồng bộ
### 4.4 Interface đồng bộ

Tiền tố đường dẫn dưới đây là quy ước; danh sách endpoint, request, response chi tiết ở B5.

| Interface | Bên cung cấp | Bên dùng | Giao thức | Xác thực | Nội dung |
| --- | --- | --- | --- | --- | --- |
| ICoreRest | core\_api, `/api/v1` | Trình duyệt qua Caddy, web khi SSR, tool của agent | HTTPS REST JSON; SSE cho trạng thái thanh toán | JWT RS256 (Guest dùng token tra đơn) | Tài khoản, catalog, giỏ, đơn, thanh toán, kho, quản trị |
| IJwks | core\_api, `/api/v1/.well-known/jwks.json` | ai\_service | HTTP GET | Công khai | Khóa công khai để kiểm JWT, ai\_service đệm lại |
| ICoreInternal | core\_api, `/internal` | ai\_service, ai\_worker | HTTP trong mạng nội bộ | Service key | Cấu hình, ảnh tham chiếu thử đồ của sản phẩm, trạng thái tài khoản |
| IPaymentWebhook | core\_api, `/api/v1/payments/webhook` | payOS | HTTPS POST | Chữ ký payOS; xử lý idempotent theo mã giao dịch | Thông báo đã thanh toán (UC08) |
| IAiRest | ai\_service, `/ai/v1` | Trình duyệt qua Caddy | HTTPS REST JSON + SSE | JWT RS256; Guest chat dùng mã phiên khách + giới hạn tần suất | Chat, xác nhận hành động, try-on, lịch sử, token webcam, nháp sản phẩm, trace |
| IAiInternal | ai\_service, `/internal` | core\_api (`ReportService`) | HTTP trong mạng nội bộ | Service key | Số liệu dùng AI theo kỳ cho UC26 |
| ITryOnCallback | ai\_service, `/ai/v1/webhooks/tryon` | Try-on provider | HTTPS POST | Bí mật hoặc chữ ký của provider; idempotent theo mã job | Kết quả job ảnh/video (UC12, UC13, UC32) |
| WebRTC | Realtime try-on provider | Trình duyệt | WebRTC | Token ngắn hạn do ai\_service cấp | Luồng camera và hình kết quả (UC33) |

