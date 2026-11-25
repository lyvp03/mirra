Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 7. Thay đổi so với entity B2
## 7. Thay đổi so với entity B2

B2 có 32 entity; B4 có 32 bảng nhưng không tương ứng một–một. Khi cập nhật sequence hoặc vẽ lại trong Astah, theo bảng này.

| Entity/thuộc tính B2 | B4 | Lý do |
| --- | --- | --- |
| Cart, Cart.guestKey | Bỏ bảng `carts`; `cart_items` khóa theo (user\_id, variant\_id) | Giỏ của Guest ở trình duyệt (B3); giỏ của người dùng chỉ có mỗi user\_id |
| AdminUnit | Tách `provinces` + `wards` | 3NF: tên tỉnh phụ thuộc mã tỉnh |
| ProductVariant.reserved | Bỏ; `stock` là số còn bán được, trừ ngay khi đặt, cộng lại khi hủy | Một cột đủ cho mọi luồng giữ chỗ/trả hàng; UC19.2 chỉ cần kiểm tra không âm |
| InventoryLedgerEntry.balanceAfter | Bỏ | Tính được từ tổng delta |
| Order.subtotal, Order.total | Bỏ | Tính từ `order_items` và `shipping_fee` |
| Order.addressSnapshot | Tách thành `receiver_name`, `receiver_phone`, `ward_code`, `street` | 1NF; ward\_code có khóa ngoại |
| OrderStatusHistory.fromStatus | Bỏ | Là trạng thái của dòng liền trước |
| Review (id, liên kết User) | Khóa (order\_id, variant\_id) trỏ về `order_items`, không lưu người viết | Người viết xác định qua đơn |
| SettingHistory.oldValue | Bỏ | Là `new_value` của dòng trước; seed ghi dòng đầu |
| User.failedLoginCount, lockedUntil | Chuyển sang bộ đếm có hạn trong Redis | Dữ liệu tạm 15 phút |
| User.locked\_reason | Thêm | UC24.2 có nhập lý do khóa |
| Category.slot | Thêm | Kiểm tra set 1 trên + 1 dưới, không nhận đầm liền (BR20) |
| Category.slot = ACCESSORY | Thêm giá trị | Giày, túi: không vào set, không thử đồ (ADR 0003) |
| ProductVariant.colorHex | Thêm `color_hex` | Swatch màu cần mã màu; catalog có sẵn (ADR 0003) |
| Product.nameVi | Thêm `name_vi` | Tên chính là tên thương mại tiếng Anh; cần tên mô tả tiếng Việt để tìm kiếm (ADR 0003) |
| ProductImage.url | Đổi thành `object_key` | URL sinh lúc đọc (bucket công khai hoặc URL ký) |
| Payment (created\_at) | Bỏ `created_at`; thêm `paid_at`, `refunded_at` | Tạo cùng đơn; UC08, UC23.2 cần thời điểm |
| UserPhoto.expiresAt | Bỏ | Bằng `created_at` + 30 ngày |
| TryOnJob.items (1..2 ProductVariant) | Bảng `tryon_job_items` | 1NF; tra cache theo món |
| TryOnJob → OutfitSuggestion | Bỏ liên kết | Không UC nào cần; món của set đã có trong `tryon_job_items` |
| WebcamBudget | Bỏ bảng | Tính từ `webcam_sessions` + trần trong `settings` |
| Conversation.messageCount, traceId | Bỏ; `trace_id` chuyển vào `chat_messages` | Đếm được; mỗi lượt trả lời có trace riêng |
| ChatMessage.toolCalls | Bỏ; thêm `guardrail_flag` | Chi tiết gọi tool đã có trên Langfuse; UC28 cần lọc tin bị chặn |
| SearchDocument (id) | Khóa (source\_type, source\_id) | Mỗi sản phẩm hoặc FAQ một tài liệu |

