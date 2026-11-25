Nguồn: 09-TESTING.md > B9 – Kế hoạch kiểm thử > Kỹ thuật thiết kế ca kiểm thử
## Kỹ thuật thiết kế ca kiểm thử

Dùng ba kỹ thuật, mỗi kỹ thuật hợp với một loại logic khác nhau.

**1. Phân vùng tương đương + giá trị biên** — cho các biến có ngưỡng số. Ví dụ:

| Biến | Vùng không hợp lệ | Vùng hợp lệ | Giá trị biên cần test |
| --- | --- | --- | --- |
| Độ dài mật khẩu | < 8 ký tự | ≥ 8 ký tự | 7, 8, 9 |
| Số lượng thêm vào giỏ so với tồn | 0 hoặc > tồn | 1..tồn | 0, 1, tồn, tồn+1 |
| Khoảng cách giao (km) | (không có) | mọi mức | 10, 30, 150, 500 (biên bậc phí) |
| Số lần đăng nhập sai / 15 phút | ≥ 5 (khóa) | < 5 | 4, 5, 6 |

**2. Bảng quyết định** — cho logic có nhiều điều kiện tổ hợp. Ví dụ: quyền bắt đầu thử đồ bằng ảnh (UC12).

| Điều kiện | R1 | R2 | R3 | R4 | R5 |
| --- | --- | --- | --- | --- | --- |
| Vai trò Customer | Không | Có | Có | Có | Có |
| Email đã xác thực | – | Không | Có | Có | Có |
| Còn lượt ảnh hôm nay | – | – | Không | Có | Có |
| Còn ngân sách AI | – | – | – | Không | Có |
| **Hành động** | Dẫn đăng nhập | Khóa, yêu cầu xác thực | Báo hết lượt | Ẩn nút (AI\_BUDGET\_EXCEEDED) | Cho thử |

**3. Chuyển trạng thái** — cho máy trạng thái đơn hàng (B6). Test cả chuyển hợp lệ và chuyển bị từ chối.

| Trạng thái hiện tại | Sự kiện | Kết quả mong đợi |
| --- | --- | --- |
| AWAITING\_PAYMENT | Thanh toán VietQR thành công | → AWAITING\_CONFIRMATION, payment = PAID |
| AWAITING\_PAYMENT | Hết hạn 15 phút | → CANCELLED, hoàn tồn kho |
| AWAITING\_CONFIRMATION | NV xác nhận | → CONFIRMED |
| AWAITING\_CONFIRMATION | Hủy đơn đã PAID | → CANCELLED, payment = REFUND\_REQUIRED |
| SHIPPING | Giao thất bại | → DELIVERY\_FAILED |
| DELIVERY\_FAILED | Hoàn về kho (đơn đã PAID) | → RETURNED, payment = REFUND\_REQUIRED (BR09) |
| DELIVERED | Chuyển về SHIPPING | Từ chối (chuyển không hợp lệ) |
| CANCELLED | Bất kỳ sự kiện | Từ chối (trạng thái cuối) |

