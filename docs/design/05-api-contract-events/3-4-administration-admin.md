Nguồn: 05-API-CONTRACT-EVENTS.md > Mirra — B5: API, contract, sự kiện > 3. Endpoint core-api > 3.4 Quản trị (Admin)
### 3.4 Quản trị (Admin)

| Method | Path | Quyền | UC | Ghi chú |
| --- | --- | --- | --- | --- |
| PUT | `/admin/products/{id}/price` | Admin | UC22.1 | `{price, publish}` |
| GET, POST | `/admin/products/{id}/promotions` | Admin | UC22.2 | 409 nếu chồng lấn |
| PATCH, DELETE | `/admin/promotions/{id}` | Admin | UC22.2 |  |
| GET | `/admin/refunds` | Admin | UC23.2 | Thanh toán REFUND\_REQUIRED |
| POST | `/admin/payments/{id}/refund` | Admin | UC23.2 | `{refund_txn_ref, note}` |
| GET | `/admin/customers`, `/admin/customers/{id}` | Admin | UC24.1 | Kèm số đơn, tổng chi |
| POST | `/admin/customers/{id}/lock`, `/unlock` | Admin | UC24.2 | `{reason}` |
| GET, POST | `/admin/staff` | Admin | UC25.1 | Tạo gửi email mời |
| PATCH | `/admin/staff/{id}` | Admin | UC25.1 |  |
| POST | `/admin/staff/{id}/lock`, `/unlock` | Admin | UC25.1 |  |
| GET | `/admin/reports/summary` | Admin | UC26 | `from, to`; gộp số liệu AI từ ai-service |
| GET | `/admin/reports/export` | Admin | UC26 | `from, to, format=csv` |
| GET | `/admin/settings` | Admin | UC27 |  |
| PUT | `/admin/settings/{key}` | Admin | UC27 | `{value}`; kiểm theo schema ở mục 7.2 |
| GET | `/admin/settings/{key}/history` | Admin | UC27 |  |

Các endpoint trên cũng là nơi tool của agent gọi tới; danh sách tool và endpoint tương ứng để B7.

