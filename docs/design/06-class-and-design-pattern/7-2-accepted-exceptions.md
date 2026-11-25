Nguồn: 06-CLASS-AND-DESIGN-PATTERN.md > Mirra — B6: Thiết kế lớp và design pattern > 7. Coupling và cohesion > 7.2 Ngoại lệ được chấp nhận
### 7.2 Ngoại lệ được chấp nhận

| Ngoại lệ | Lý do | Giới hạn |
| --- | --- | --- |
| Ordering dùng `VariantRepository` của Catalog | Trừ tồn cần khóa dòng biến thể trong cùng transaction đặt hàng | Chỉ `lock_many`, `get_many`; mọi thay đổi `stock` qua `StockPolicy` |
| Administration đọc `OrderRepository` | Báo cáo cần truy vấn tổng hợp trên đơn | Chỉ method tổng hợp, không ghi |
| Observability đọc repository của TryOn, Webcam, Assistant | Số liệu UC26 | Chỉ đếm, không ghi |
| Webcam dùng `SetRule`, `OutfitComposer`, `TryOnJobRepository` của TryOn | Cùng quy tắc set và cùng bảng lịch sử (`WEBCAM_SNAPSHOT`) | Chỉ tạo job COMPLETED cho khung hình |

Thêm một ngoại lệ đọc: `ReviewRepository.eligible_item` của Catalog đọc `orders`, `order_items` để xác minh quyền đánh giá, thay vì gọi `OrderService`.

Với các ngoại lệ trên, phụ thuộc giữa component của core-api chỉ đi một chiều: Ordering → Catalog, Administration → Ordering; Identity độc lập. Trong ai-service: Assistant → Knowledge, Webcam → TryOn, Observability → TryOn, Webcam, Assistant (chỉ đọc). `CostRecorder` và `PriceTable` đặt trong package `core` dùng chung của ai-service (không thuộc Observability) để TryOn, Webcam, Knowledge, Assistant ghi chi phí mà không tạo vòng với Observability. Không có vòng.

