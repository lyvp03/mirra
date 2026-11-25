Nguồn: 05-API-CONTRACT-EVENTS.md > Mirra — B5: API, contract, sự kiện > 2. Xác thực và phân quyền > 2.6 Ký hiệu quyền trong bảng endpoint
### 2.6 Ký hiệu quyền trong bảng endpoint

| Ký hiệu | Ai được gọi |
| --- | --- |
| Public | Không cần token |
| Owner | Customer sở hữu tài nguyên, hoặc Guest có `X-Order-Token` đúng đơn |
| Customer | Customer đã đăng nhập |
| Verified | Customer đã xác thực email (BR19) |
| Staff | Staff hoặc Admin |
| Admin | Chỉ Admin |
| Any | Guest có phiên chat hoặc bất kỳ người đã đăng nhập |
| Service | Gọi nội bộ bằng service key |

