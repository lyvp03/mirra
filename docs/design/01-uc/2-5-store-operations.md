Nguồn: 01-UC.md > Mirra — B1: Phân rã và đặc tả use case > 2. Phân rã use case > 2.5 Vận hành cửa hàng
### 2.5 Vận hành cửa hàng

```mermaid
flowchart LR
  S((Staff / Admin)) --- U17([UC17 Quản lý sản phẩm])
  U17 --> U171([UC17.1 Thêm sản phẩm])
  U17 --> U172([UC17.2 Sửa sản phẩm, ẩn hiện])
  U17 --> U173([UC17.3 Quản lý biến thể và ảnh])
  U17 --> U174([UC17.4 Bật tắt thử đồ])
  U18([UC18 Tạo sản phẩm nháp bằng AI]) -. extend .-> U171
  S --- U19([UC19 Quản lý tồn kho])
  U19 --> U191([UC19.1 Xem tồn, hàng sắp hết])
  U19 --> U192([UC19.2 Nhập kho, điều chỉnh tồn])
  U19 --> U193([UC19.3 Xem sổ kho])
  S --- U20([UC20 Xử lý đơn hàng])
  U20 --> U201([UC20.1 Xem, lọc đơn])
  U20 --> U202([UC20.2 Xác nhận đơn])
  U20 --> U203([UC20.3 Cập nhật giao hàng])
  U20 --> U204([UC20.4 Hủy đơn chờ xác nhận])
  U20 --> U205([UC20.5 Ghi nhận giao thất bại, hoàn hàng])
  S --- U21([UC21 Quản lý FAQ và chính sách])
  U21 --> U211([UC21.1 Thêm, sửa, xóa bài])
```

| UC | Quan hệ | Điều kiện, ghi chú | Giai đoạn |
| --- | --- | --- | --- |
| UC17.1–UC17.4 | UC con của UC17 | Staff không sửa giá; sản phẩm mới ở trạng thái Nháp | MVP |
| UC18 Tạo nháp bằng AI | «extend» UC17.1 | Khi Staff tải ảnh và bấm "Tạo nháp bằng AI" | Mở rộng |
| UC19.1–UC19.3 | UC con của UC19 | Mọi điều chỉnh bắt buộc ghi lý do | MVP |
| UC20.1–UC20.5 | UC con của UC20 | UC20.2 với đơn COD của Guest: gọi xác nhận trước (BR13) | MVP |
| UC21.1 | UC con của UC21 | Lưu xong phát sự kiện để ai-service cập nhật chỉ mục | MVP |

