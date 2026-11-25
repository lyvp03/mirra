Nguồn: 05-API-CONTRACT-EVENTS.md > Mirra — B5: API, contract, sự kiện > 3. Endpoint core-api > 3.3 Vận hành (Staff)
### 3.3 Vận hành (Staff)

| Method | Path | Quyền | UC | Ghi chú |
| --- | --- | --- | --- | --- |
| GET, POST | `/admin/products` | Staff | UC17.1 | Tạo ở trạng thái HIDDEN |
| GET, PATCH, DELETE | `/admin/products/{id}` | Staff | UC17.2 | PATCH được ẩn/hiện sản phẩm đã có giá; DELETE trả 409 nếu đã có đơn |
| POST | `/admin/products/{id}/variants` | Staff | UC17.3 |  |
| PATCH, DELETE | `/admin/variants/{id}` | Staff | UC17.3 | Không sửa `stock` ở đây (dùng UC19.2) |
| POST | `/admin/products/{id}/images` | Staff | UC17.3 | multipart; `kind`, `color` |
| PATCH, DELETE | `/admin/images/{id}` | Staff | UC17.3 | Đổi thứ tự |
| PUT | `/admin/products/{id}/try-on` | Staff | UC17.4 | `{enabled}`; 409 `FLAT_LAY_REQUIRED` nếu sản phẩm thuộc danh mục ACCESSORY hoặc có màu thiếu ảnh tham chiếu thử đồ (flat-lay hoặc ảnh người mẫu) |
| PATCH | `/admin/reviews/{order_id}/{variant_id}` | Staff | UC11 | `{hidden}` |
| GET | `/admin/inventory` | Staff | UC19.1 | `low_stock=true` |
| POST | `/admin/inventory/adjustments` | Staff | UC19.2 | `{variant_id, delta, reason, note}` |
| GET | `/admin/inventory/ledger` | Staff | UC19.3 | `variant_id, from, to` |
| GET | `/admin/orders`, `/admin/orders/{id}` | Staff | UC20.1 | Lọc `status, from, to, q` |
| POST | `/admin/orders/{id}/confirm` | Staff | UC20.2 | `{phone_call_checked}` bắt buộc với đơn COD của Guest (BR13) |
| POST | `/admin/orders/{id}/ship` | Staff | UC20.3 | `{tracking_no}` |
| POST | `/admin/orders/{id}/deliver` | Staff | UC20.3 | COD → thanh toán PAID |
| POST | `/admin/orders/{id}/cancel` | Staff / Admin | UC20.4, UC23.1 | `{reason}`; Staff hủy đơn chờ xác nhận, Admin hủy thêm được đơn đã xác nhận, đang giao |
| POST | `/admin/orders/{id}/delivery-failed` | Staff | UC20.5 | `{reason}` |
| POST | `/admin/orders/{id}/return` | Staff | UC20.5 | Nhận hàng về kho, cộng tồn |
| GET, POST | `/admin/faqs` | Staff | UC21 |  |
| PATCH, DELETE | `/admin/faqs/{id}` | Staff | UC21 |  |

