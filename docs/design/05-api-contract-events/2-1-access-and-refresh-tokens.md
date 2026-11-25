Nguồn: 05-API-CONTRACT-EVENTS.md > Mirra — B5: API, contract, sự kiện > 2. Xác thực và phân quyền > 2.1 Access token và refresh token
### 2.1 Access token và refresh token

| Token | Nơi giữ | Gửi thế nào | Hạn |
| --- | --- | --- | --- |
| Access (JWT RS256) | Bộ nhớ JS của web (không localStorage) | Header `Authorization: Bearer <jwt>` tới `/api/v1` và `/ai/v1` | 15 phút |
| Refresh (chuỗi ngẫu nhiên) | Cookie `mirra_refresh`: `HttpOnly; Secure; SameSite=Strict; Path=/api/v1/auth` | Trình duyệt tự gửi khi gọi `/api/v1/auth/refresh`, `/logout` | 7 ngày; lưu hash trong `auth_tokens` |

Luồng:

1. `POST /auth/login` trả access token trong body và đặt cookie refresh.
2. Khi tải lại trang hoặc access sắp hết hạn, web gọi `POST /auth/refresh` để nhận access mới. Mỗi lần refresh đổi luôn refresh token (token cũ gán `used_at`). Dùng lại một refresh token đã dùng → thu hồi mọi refresh token của người đó, bắt đăng nhập lại.
3. `POST /auth/logout` thu hồi token và xóa cookie.
4. Admin khóa tài khoản (UC24.2, UC25) thu hồi mọi refresh token; access token đang có còn dùng được tối đa 15 phút, chấp nhận được với phạm vi đồ án.
5. Web SSR chỉ render dữ liệu công khai (danh mục, sản phẩm); trang của riêng người dùng lấy dữ liệu ở trình duyệt.

