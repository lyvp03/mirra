Nguồn: 03-PACKAGE-COMPONENT-DEPLOYMENT.md > Mirra — B3: Package, Component, Deployment > 5. Sơ đồ deployment > 5.4 Cấu hình và bí mật
### 5.4 Cấu hình và bí mật

Bí mật nằm trong file môi trường trên VPS, không đưa vào git. Mỗi container chỉ nhận phần nó cần:

| Bí mật | core-api, core-worker | ai-service, ai-worker |
| --- | --- | --- |
| Mật khẩu DB user của schema mình | có | có |
| Khóa riêng ký JWT | có | không (chỉ đọc JWKS) |
| Service key cho `/internal` | có | có |
| payOS, SMTP | có | không |
| Khóa LLM, embedding, try-on, realtime, Langfuse | không | có |
| Khóa MinIO | có (bucket `products`) | có (bucket `tryon`, đọc `products`) |

