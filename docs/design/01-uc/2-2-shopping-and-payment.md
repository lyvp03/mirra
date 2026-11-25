Nguồn: 01-UC.md > Mirra — B1: Phân rã và đặc tả use case > 2. Phân rã use case > 2.2 Mua hàng và thanh toán
### 2.2 Mua hàng và thanh toán

```mermaid
flowchart LR
  G((Guest / Customer)) --- U05([UC05 Xem, tìm kiếm sản phẩm])
  U05 --> U051([UC05.1 Tìm kiếm, lọc, sắp xếp])
  U05 --> U052([UC05.2 Xem chi tiết, chọn màu và size])
  G --- U06([UC06 Quản lý giỏ hàng])
  U06 --> U061([UC06.1 Thêm vào giỏ])
  U06 --> U062([UC06.2 Sửa số lượng, xóa])
  U063([UC06.3 Gộp giỏ khi đăng nhập]) -. extend .-> U06
  G --- U07([UC07 Đặt hàng])
  U07 -. include .-> U071([UC07.1 Kiểm tra tồn kho và giá])
  U07 -. include .-> U072([UC07.2 Tính phí giao hàng])
  U07 -. include .-> U073([UC07.3 Gửi email xác nhận])
  U08([UC08 Thanh toán VietQR]) -. extend .-> U07
  U08 --- P((payOS))
  G --- U09([UC09 Theo dõi đơn hàng])
  U10([UC10 Hủy đơn hàng]) -. extend .-> U09
  U11([UC11 Đánh giá sản phẩm]) -. extend .-> U09
  T((Bộ hẹn giờ)) --- U29([UC29 Tự hủy đơn quá hạn])
```

| UC | Quan hệ | Điều kiện, ghi chú | Giai đoạn |
| --- | --- | --- | --- |
| UC05.1, UC05.2 | UC con của UC05 |  | MVP |
| UC06.1, UC06.2 | UC con của UC06 | Guest: giỏ ở trình duyệt; Customer: giỏ trên server | MVP |
| UC06.3 Gộp giỏ | «extend» UC06 | Khi Guest có giỏ rồi đăng nhập | MVP |
| UC07.1–UC07.3 | «include» UC07 |  | MVP |
| UC08 Thanh toán VietQR | «extend» UC07 | Khi khách chọn VietQR | MVP |
| UC09 Theo dõi đơn |  | Customer xem lịch sử đơn; Guest mở link có token | MVP |
| UC10 Hủy đơn | «extend» UC09 | Đơn còn Chờ thanh toán hoặc Chờ xác nhận | MVP |
| UC11 Đánh giá | «extend» UC09 | Đơn đã Hoàn thành, chỉ Customer | Mở rộng |
| UC29 Tự hủy đơn | Bộ hẹn giờ | Đơn VietQR quá 15 phút chưa trả | MVP |

