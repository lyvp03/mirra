Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 4. Từ điển dữ liệu schema core > 4.18 settings, setting\_history — cấu hình (UC27)
### 4.18 settings, setting\_history — cấu hình (UC27)

| Bảng.cột | Kiểu | Ràng buộc | Ý nghĩa |
| --- | --- | --- | --- |
| settings.key | varchar(50) | PK | Ví dụ `tryon.daily_image_quota`, `shipping.tiers` |
| settings.value | jsonb |  | Số, bảng phí ship hoặc cờ bật tắt; kiểm tra theo schema của từng key ở ứng dụng |
| setting\_history.setting\_key | varchar(50) | FK settings |  |
| setting\_history.new\_value | jsonb |  | Giá trị cũ là dòng liền trước; seed ghi dòng đầu tiên |
| setting\_history.actor\_id | uuid | NULL, FK users | Rỗng với dòng do seed tạo |

`settings` không có `id`, `created_at`.

