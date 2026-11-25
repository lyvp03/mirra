Nguồn: 01-UC.md > Mirra — B1: Phân rã và đặc tả use case > 2. Phân rã use case > 2.6 Quản trị hệ thống
### 2.6 Quản trị hệ thống

```mermaid
flowchart LR
  AD((Admin)) --- U22([UC22 Quản lý giá và khuyến mãi])
  U22 --> U221([UC22.1 Đặt giá, công khai sản phẩm])
  U22 --> U222([UC22.2 Tạo, sửa giá khuyến mãi])
  AD --- U23([UC23 Hủy đơn đã xác nhận và hoàn tiền])
  U23 --> U231([UC23.1 Hủy đơn đã xác nhận])
  U23 --> U232([UC23.2 Xác nhận đã hoàn tiền])
  AD --- U24([UC24 Quản lý khách hàng])
  U24 --> U241([UC24.1 Xem, tìm khách hàng])
  U24 --> U242([UC24.2 Khóa, mở tài khoản])
  AD --- U25([UC25 Quản lý nhân viên])
  U25 --> U251([UC25.1 Thêm, sửa, khóa nhân viên])
  AD --- U26([UC26 Xem báo cáo])
  AD --- U27([UC27 Cấu hình hệ thống])
  AD --- U28([UC28 Xem trace của trợ lý])
```

| UC | Quan hệ | Điều kiện, ghi chú | Giai đoạn |
| --- | --- | --- | --- |
| UC22.1, UC22.2 | UC con của UC22 |  | MVP |
| UC23.1, UC23.2 | UC con của UC23 | UC23.2 khi thanh toán ở trạng thái Cần hoàn tiền | MVP |
| UC24.1 | UC con của UC24 | Staff cũng xem được | MVP |
| UC24.2 | UC con của UC24 | Chỉ Admin | MVP |
| UC25.1 | UC con của UC25 |  | MVP |
| UC26 Xem báo cáo |  | Doanh thu, top sản phẩm, tỉ lệ thử đồ rồi mua, chi phí AI | Mở rộng |
| UC27 Cấu hình |  | Quota thử đồ, hạn mức chat, bảng phí vùng và ngưỡng miễn phí ship, bảng size | MVP |
| UC28 Xem trace |  | Mở trace của một hội thoại | Mở rộng |

