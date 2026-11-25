Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 8. Index, quy tắc xóa, dữ liệu seed > 8.2 Quy tắc xóa
### 8.2 Quy tắc xóa

- Không xóa cứng `users`, `orders`, `payments`, `inventory_ledger`: tài khoản thì khóa (`status`), đơn thì hủy (`status`).
- "Xóa" sản phẩm trong giao diện là chuyển HIDDEN. Chỉ xóa cứng được sản phẩm chưa có đơn; khi có đơn, khóa ngoại từ `order_items` (mặc định RESTRICT) chặn lại.
- `ON DELETE CASCADE` chỉ cho bảng con không có ý nghĩa khi mất cha: `auth_tokens`, `addresses`, `cart_items`, `product_variants`, `product_images`, `promotions`, `order_items`, `order_status_history`, `reviews`, `tryon_job_items`, `chat_messages`, `pending_actions`, `outfit_suggestions`.
- `ON DELETE SET NULL` cho liên kết của `ai_cost_records`, để số liệu chi phí còn lại.
- Các khóa ngoại còn lại dùng mặc định RESTRICT.
- File trên MinIO xóa bởi service (UC14.2, UC30) rồi đánh dấu `deleted_at` hoặc `media_deleted_at`; không dựa vào xóa dòng.

