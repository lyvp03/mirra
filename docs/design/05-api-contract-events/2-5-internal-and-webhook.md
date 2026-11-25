Nguồn: 05-API-CONTRACT-EVENTS.md > Mirra — B5: API, contract, sự kiện > 2. Xác thực và phân quyền > 2.5 Nội bộ và webhook
### 2.5 Nội bộ và webhook

| Kênh | Xác thực |
| --- | --- |
| `/internal/v1` hai chiều | Header `X-Service-Key`, mỗi chiều một khóa riêng từ biến môi trường. Caddy chỉ định tuyến `/api` và `/ai` nên `/internal` không ra Internet |
| Webhook payOS | Kiểm chữ ký bằng checksum key của payOS, kiểm số tiền khớp `payments.amount` |
| Webhook try-on provider | Bí mật hoặc chữ ký theo provider chọn sau benchmark |

