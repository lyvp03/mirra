Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 4. Từ điển dữ liệu schema core > 4.11 orders — đơn hàng (UC07–UC10, UC20, UC23, UC29)
### 4.11 orders — đơn hàng (UC07–UC10, UC20, UC23, UC29)

| Cột | Kiểu | Ràng buộc | Ý nghĩa |
| --- | --- | --- | --- |
| code | varchar(12) | UNIQUE | Mã đơn 10 chữ số, hiển thị cho khách và dùng làm orderCode của payOS (chốt ở B5) |
| user\_id | uuid | NULL, FK users | Rỗng với đơn của Guest |
| guest\_email | varchar(255) | NULL |  |
| guest\_token\_hash | char(64) | NULL | Token trong link tra đơn của Guest |
| receiver\_name | varchar(100) |  |  |
| receiver\_phone | varchar(15) |  |  |
| ward\_code | varchar(10) | FK wards |  |
| street | varchar(255) |  |  |
| shipping\_fee | integer | CHECK ≥ 0 | Phí tính lúc đặt |
| status | varchar(25) | CHECK 8 trạng thái đơn (B2 mục 8.1) |  |
| tracking\_no | varchar(50) | NULL | UC20.3 |
| updated\_at | timestamptz |  |  |

Ràng buộc bảng: `CHECK (user_id IS NOT NULL OR (guest_email IS NOT NULL AND guest_token_hash IS NOT NULL))`. Tiền hàng và tổng tiền không lưu, tính từ `order_items` và `shipping_fee`. Hạn thanh toán (UC29) tính từ `created_at` cộng thời gian chờ trong `settings`. Hạn link tra đơn của Guest (BR12) cũng không cần cột riêng: lấy `created_at` của dòng `order_status_history` đưa đơn vào trạng thái cuối (DELIVERED, CANCELLED, RETURNED), cộng `order.guest_link_days` trong `settings` (index `(order_id, created_at)` đã có).

