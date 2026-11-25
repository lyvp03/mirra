Nguồn: 05-API-CONTRACT-EVENTS.md > Mirra — B5: API, contract, sự kiện > 3. Endpoint core-api > 3.1 Xác thực và tài khoản (Identity)
### 3.1 Xác thực và tài khoản (Identity)

| Method | Path | Quyền | UC | Ghi chú |
| --- | --- | --- | --- | --- |
| POST | `/auth/register` | Public | UC01 | 201; gửi email xác thực |
| POST | `/auth/verify-email` | Public | UC01.1 | Body `{token}` |
| POST | `/auth/resend-verification` | Customer | UC01.1 |  |
| POST | `/auth/login` | Public | UC02 | Trả access token, đặt cookie refresh |
| POST | `/auth/refresh` | Cookie | UC02 | Đổi refresh token mỗi lần |
| POST | `/auth/logout` | Customer, Staff | UC02 |  |
| POST | `/auth/password/forgot` | Public | UC03 | Luôn 202, không tiết lộ email có tồn tại |
| POST | `/auth/password/reset` | Public | UC03 | Body `{token, new_password}` |
| POST | `/auth/password/set` | Public | UC25 | Staff đặt mật khẩu từ link mời |
| GET | `/.well-known/jwks.json` | Public | — | Khóa công khai cho ai-service |
| GET, PATCH | `/me` | Customer, Staff | UC04 | Họ tên, số điện thoại |
| POST | `/me/password` | Customer, Staff | UC04.1 | `{current_password, new_password}` |
| GET, POST | `/me/addresses` | Customer | UC04.2 | Tối đa 5 |
| PATCH, DELETE | `/me/addresses/{id}` | Customer | UC04.2 |  |
| GET | `/provinces`, `/provinces/{code}/wards` | Public | UC04, UC07 | Form địa chỉ |
| GET | `/settings/public` | Public | — | Cờ bật tắt tính năng và hạn mức để web hiển thị |

