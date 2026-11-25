Nguồn: 05-API-CONTRACT-EVENTS.md > Mirra — B5: API, contract, sự kiện > 1. Quy ước chung > 1.1 Địa chỉ
### 1.1 Địa chỉ

| API | Địa chỉ | Ai gọi |
| --- | --- | --- |
| core-api công khai | `https://<domain>/api/v1` | Trình duyệt, web khi SSR (`http://core-api:8000/api/v1`), tool của agent |
| ai-service công khai | `https://<domain>/ai/v1` | Trình duyệt |
| core-api nội bộ | `http://core-api:8000/internal/v1` | ai-service, ai-worker |
| ai-service nội bộ | `http://ai-service:8001/internal/v1` | core-api (báo cáo) |
| Webhook | `/api/v1/payments/payos/webhook`, `/ai/v1/webhooks/tryon` | payOS, try-on provider |

Web và hai API cùng tên miền qua Caddy nên không cần CORS ở production; môi trường dev cho phép `http://localhost:3000`. Đổi phiên bản không tương thích thì thêm `/v2`, không sửa `/v1`.

