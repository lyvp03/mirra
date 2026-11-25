Nguồn: 02-BCE-AND-SEQUENCE.md > Mirra — B2: Phân tích BCE và sequence > 8. Sơ đồ lớp phân tích gộp > 8.3 Control dùng chung
### 8.3 Control dùng chung

| Control | Được gọi từ | Entity và thao tác | Vai trò |
| --- | --- | --- | --- |
| StockPolicy | UC07, UC08, UC10, UC19, UC20, UC23, UC29 | ProductVariant (R, U), InventoryLedgerEntry (C), Setting (R) | Giữ chỗ, trả hàng về kho, ngưỡng sắp hết |
| ShippingFeeCalculator | UC07 | AdminUnit, Setting (R) | Phí ship theo khoảng cách (BR11) |
| OrderStateMachine | UC08, UC10, UC20, UC23, UC29 | Không | Kiểm tra chuyển trạng thái đơn hợp lệ và ai được chuyển |
| TryOnQuotaPolicy | UC12, UC13, UC32 | TryOnJob, Setting (R) | 5 ảnh và 2 video mỗi ngày, hoàn lượt khi lỗi |
| ImageValidator | UC12, UC14, UC17, UC18, UC32 | Không | Định dạng, dung lượng ≤ 5 MB, ảnh người hợp lệ |
| OutfitComposer | UC32, UC33 | ProductImage (R) | Chuẩn bị ảnh tham chiếu của set (BR20) |
| Guardrail | UC15 | Không | Lọc đầu vào, đầu ra của trợ lý |
| ToolRegistry | UC15, UC16 | Không | Chọn bộ công cụ theo vai trò, gọi control nghiệp vụ |
| AccessPolicy | UC15, UC16 | Không | Kiểm tra quyền theo người dùng thật (BR17) |
