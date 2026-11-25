Nguồn: 05-API-CONTRACT-EVENTS.md > Mirra — B5: API, contract, sự kiện > 1. Quy ước chung > 1.5 Chống gửi trùng và giới hạn tần suất
### 1.5 Chống gửi trùng và giới hạn tần suất

- `POST /orders` và các `POST` tạo job thử đồ nhận header `Idempotency-Key` (UUID do web sinh mỗi lần bấm). Cùng khóa trong 24 giờ trả lại kết quả lần đầu; lưu trong Redis.
- Webhook xử lý idempotent theo `payments.txn_id` và `tryon_jobs.provider_ref`.
- Giới hạn theo IP cho đăng nhập, đăng ký, quên mật khẩu, gửi lại email xác thực; giới hạn chung cho mọi endpoint công khai. Con số cụ thể là cấu hình triển khai, không phải quy tắc nghiệp vụ.
- Hạn mức nghiệp vụ (lượt thử đồ, tin chat, phiên webcam) lấy từ `settings` và trả 429 với `code` riêng.

