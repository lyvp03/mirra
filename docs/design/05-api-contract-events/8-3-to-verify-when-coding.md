Nguồn: 05-API-CONTRACT-EVENTS.md > Mirra — B5: API, contract, sự kiện > 8. File OpenAPI và điểm cần kiểm chứng > 8.3 Cần kiểm chứng khi code
### 8.3 Cần kiểm chứng khi code

| Điểm | Kiểm bằng |
| --- | --- |
| Tên trường webhook payOS (`orderCode`, `amount`, `reference`, `signature`) và cách tính chữ ký | Tài liệu và SDK payOS lúc tích hợp; schema `PayosWebhook` cho phép thêm trường |
| Body webhook của try-on provider, dữ liệu `provider_session` của dịch vụ realtime | Benchmark 31/10 – 06/11; hai chỗ này để dạng object mở trong OpenAPI |
| Provider realtime có báo thời lượng thực tế không | Benchmark; nếu không thì dùng `used_seconds` web gửi lên, chặn trong khoảng cho phép |
| Caddy không buffer SSE qua cả ba đường dẫn stream | Thử trên môi trường dev với Compose đầy đủ |
