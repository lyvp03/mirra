Nguồn: 05-API-CONTRACT-EVENTS.md > Mirra — B5: API, contract, sự kiện > 2. Xác thực và phân quyền > 2.2 Nội dung JWT
### 2.2 Nội dung JWT

| Claim | Giá trị |
| --- | --- |
| header `kid` | Mã khóa ký; JWKS công bố khóa hiện tại và khóa trước đó để đổi khóa không làm rơi phiên |
| `iss` | `mirra-core` |
| `aud` | `["mirra-core", "mirra-ai"]` |
| `sub` | `users.id` |
| `role` | `CUSTOMER`, `STAFF`, `ADMIN` |
| `email_verified` | `true`/`false`; sau khi xác thực email, web gọi refresh để nhận token mới |
| `iat`, `exp`, `jti` | Chuẩn |

ai-service kiểm chữ ký bằng `GET /api/v1/.well-known/jwks.json` (đệm 10 phút, tải lại khi gặp `kid` lạ), kiểm `aud` có `mirra-ai` và `exp`. ai-service không tự cấp token.

