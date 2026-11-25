Nguồn: 05-API-CONTRACT-EVENTS.md > Mirra — B5: API, contract, sự kiện > 4. Endpoint ai-service và endpoint nội bộ > 4.2 core-api nội bộ (`/internal/v1`, Service)
### 4.2 core-api nội bộ (`/internal/v1`, Service)

| Method | Path | Người gọi | Dùng cho |
| --- | --- | --- | --- |
| GET | `/settings` | ai-service, ai-worker | Đọc toàn bộ cấu hình, đệm trong Redis; làm mới khi nhận sự kiện `settings.updated` |
| GET | `/variants?ids=a,b` | ai-service | Thông tin món cho try-on, set, webcam, gợi ý: `product_id, product_name, slot, color, size, effective_price, in_stock, published, try_on_enabled, tryon_image_url` (ảnh tham chiếu thử đồ: flat-lay nếu có, không thì ảnh người mẫu chính diện) |
| GET | `/index-documents/{source_type}/{id}` | ai-worker | Nội dung mới nhất của sản phẩm hoặc FAQ để tạo embedding, kèm `visible`; 404 = đã xóa |

B3 có nhắc "trạng thái tài khoản" trong ICoreInternal; B5 bỏ endpoint này vì `role` và `email_verified` đã có trong JWT.

