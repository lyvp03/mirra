Nguồn: 05-API-CONTRACT-EVENTS.md > Mirra — B5: API, contract, sự kiện > 5. Contract các luồng chính > 5.1 Đặt hàng và thanh toán VietQR (UC07, UC08)
### 5.1 Đặt hàng và thanh toán VietQR (UC07, UC08)

1. Web gọi `POST /api/v1/checkout/quote` mỗi khi đổi địa chỉ hoặc giỏ.
2. Người mua bấm đặt: `POST /api/v1/orders` với `Idempotency-Key` và `expected_total` bằng tổng đang hiển thị.
3. VietQR: response có `payment.qr_code`, web vẽ QR và mở `GET /orders/{code}/payment/stream`. COD: chuyển thẳng trang cảm ơn.
4. payOS gọi webhook → core cập nhật thanh toán và đơn, phát pub/sub → stream gửi `payment.status` = PAID.

Ví dụ đặt hàng của Guest:

```json
POST /api/v1/orders
Idempotency-Key: 6a1f0c2e-...
{
  "lines": [{"variant_id": "8f1c...", "quantity": 1}, {"variant_id": "2b7d...", "quantity": 1}],
  "address": {"receiver_name": "Nguyễn An", "receiver_phone": "0912345678", "ward_code": "00123", "street": "12 ngõ 5 Giải Phóng"},
  "guest_email": "an@example.com",
  "payment_method": "VIETQR",
  "expected_total": 445000
}

201
{
  "order": {"id": "c0de...", "code": "2611031042", "status": "AWAITING_PAYMENT", "subtotal": 420000, "shipping_fee": 25000, "total": 445000, "created_at": "2026-11-03T08:15:00Z"},
  "payment": {"method": "VIETQR", "status": "UNPAID", "amount": 445000, "qr_code": "000201...", "checkout_url": "https://pay.payos.vn/...", "expires_at": "2026-11-03T08:30:00Z"},
  "order_token": "r9Kx..."
}
```

| Lỗi | HTTP | Khi nào |
| --- | --- | --- |
| `PRICE_CHANGED` | 409 | `expected_total` khác tổng server; web gọi lại quote và hiện thay đổi (UC07.1) |
| `OUT_OF_STOCK` | 409 | Không trừ được tồn cho một dòng; `errors[].field` chỉ dòng đó |
| `PRODUCT_UNAVAILABLE` | 409 | Sản phẩm bị ẩn trong lúc mua |
| `INVALID_WARD` | 422 | Mã phường/xã không có |
| `PAYMENT_GATEWAY_ERROR` | 502 | Không tạo được link payOS; đơn vẫn tạo, web cho thử lại ở trang thanh toán |

`orders.code` là 10 chữ số vì payOS yêu cầu `orderCode` là số nguyên; cùng một mã dùng cho khách và cho payOS. Webhook khớp `data.orderCode` với `orders.code`, kiểm `data.amount` bằng `payments.amount`, lưu `data.reference` vào `payments.txn_id` (UNIQUE nên nhận trùng không xử lý lại). Thanh toán đến sau khi đơn đã tự hủy xử lý như B2 UC08.

