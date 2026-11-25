Nguồn: 05-API-CONTRACT-EVENTS.md > Mirra — B5: API, contract, sự kiện > 1. Quy ước chung > 1.4 Lỗi
### 1.4 Lỗi

Mọi lỗi trả `application/problem+json` (RFC 9457) cộng trường `code` để web hiển thị thông báo theo ngôn ngữ; `detail` chỉ dành cho lập trình viên.

```json
{
  "type": "https://<domain>/errors/out-of-stock",
  "title": "Out of stock",
  "status": 409,
  "code": "OUT_OF_STOCK",
  "detail": "Variant 8f1c... has 0 left",
  "errors": [{"field": "lines[0].quantity", "message": "exceeds stock"}]
}
```

| HTTP | Dùng khi |
| --- | --- |
| 400 | Yêu cầu sai nghiệp vụ (link hết hạn, không đủ điều kiện) |
| 401 | Thiếu hoặc sai access token |
| 403 | Đúng token nhưng không đủ quyền, hoặc chưa xác thực email khi thử đồ |
| 404 | Không tìm thấy, hoặc không phải của người gọi (không tiết lộ tồn tại) |
| 409 | Xung đột trạng thái: hết hàng, đơn không ở trạng thái cho phép, email trùng |
| 413, 415 | File quá lớn, sai định dạng |
| 422 | Sai kiểu, thiếu trường (kiểm tra Pydantic) |
| 429 | Vượt giới hạn tần suất hoặc hết lượt/hạn mức; có header `Retry-After` |
| 502, 503 | Dịch vụ ngoài lỗi hoặc tính năng đang tắt |

Danh sách `code` ở mục 7.

