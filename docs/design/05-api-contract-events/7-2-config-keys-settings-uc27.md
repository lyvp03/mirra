Nguồn: 05-API-CONTRACT-EVENTS.md > Mirra — B5: API, contract, sự kiện > 7. Mã lỗi và khóa cấu hình > 7.2 Khóa cấu hình (`settings`, UC27)
### 7.2 Khóa cấu hình (`settings`, UC27)

B4 để lại tên khóa và kiểu giá trị cho B5. Mặc định lấy từ B1 mục 6.2, 6.3 và các quy tắc BR; `SettingsService` kiểm giá trị theo cột "Kiểu" trước khi ghi. Thông số bảo mật (hạn token, số lần đăng nhập sai, độ dài mật khẩu) là hằng số cấu hình triển khai, không để Admin sửa trên giao diện.

| Khóa | Kiểu | Mặc định | Công khai | Dùng ở |
| --- | --- | --- | --- | --- |
| `tryon.enabled` | boolean | true | có | UC12–UC14, UC32 |
| `tryon.daily_image_quota` | integer 0–50 | 5 | có | UC12.3, UC32 |
| `tryon.daily_video_quota` | integer 0–20 | 2 | có | UC13 |
| `tryon.terms_version` | string | phiên bản điều khoản khi phát hành | có | UC12.1 |
| `photo.retention_days` | integer 1–30 | 30 | có | UC30 |
| `webcam.enabled` | boolean | true | có | UC33 |
| `webcam.session_seconds` | integer 5–60 | 20 | có | UC33 |
| `webcam.daily_sessions` | integer 0–5 | 1 | có | UC33 |
| `webcam.budget_seconds` | integer ≥ 0 | 250 | không | UC33 |
| `ai.budget_usd_month` | number ≥ 0 | 100 (cảnh báo từ 80%) | không | NFR13, UC26 |
| `chat.guest_session_limit` | integer | 20 | có | UC15 |
| `chat.customer_daily_limit` | integer | 50 | có | UC15 |
| `chat.staff_daily_limit` | integer | 200 | không | UC15 |
| `chat.action_ttl_minutes` | integer 1–60 | 10 | không | UC15 (B7 mục 2.6) |
| `chat.conversation_idle_days` | integer 1–90 | 7 | không | UC15 (B7 mục 3.6) |
| `inventory.low_stock_threshold` | integer ≥ 0 | 3 | không | UC19.1 |
| `order.payment_timeout_minutes` | integer 5–60 | 15 (bằng hạn QR ở UC08) | có | UC08, UC29 |
| `order.guest_link_days` | integer 1–30 | 7 (tính từ lúc đơn vào trạng thái cuối) | không | BR12 (Guest tra, hủy đơn) |
| `shipping.warehouse_location` | `{lat, lng}` | tọa độ kho khu vực Hoàng Mai, nhập khi seed | không | UC07.2 |
| `shipping.road_factor` | number 1–2 | 1.3 | không | UC07.2 |
| `shipping.tiers` | `[{max_km, fee}]`, bậc cuối `max_km: null` | 10→18000, 30→25000, 150→30000, 500→35000, null→40000 | không | UC07.2 |
| `shipping.weight_surcharge` | `{free_grams, step_grams, fee_per_step}` | 1000, 500, 5000 | không | UC07.2 |
| `shipping.free_rules` | `[{min_subtotal, max_km}]` | 499000 trong 30 km; 799000 mọi khoảng cách (`max_km: null`) | có | UC07.2 |

Cột "Công khai" là các khóa trả qua `GET /api/v1/settings/public` để web hiện nút, hạn mức và ngưỡng miễn phí ship.

