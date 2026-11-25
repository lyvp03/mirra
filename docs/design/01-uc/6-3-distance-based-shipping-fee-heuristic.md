Nguồn: 01-UC.md > Mirra — B1: Phân rã và đặc tả use case > 6. Giả định cần kiểm chứng và giá trị đã chốt > 6.3 Phí giao hàng theo khoảng cách (heuristic)
### 6.3 Phí giao hàng theo khoảng cách (heuristic)

Phí ship tính theo khoảng cách từ kho (khu vực Hoàng Mai, Hà Nội; Admin cấu hình được) tới địa chỉ nhận, cộng phụ phí cân nặng. Đây là cách tính giả lập, thay cho API hãng vận chuyển, và đặt sau adapter `ShippingFeeStrategy` nên sau này đổi sang GHN không sửa nghiệp vụ.

Cách tính khoảng cách:

1. Mỗi Phường/Xã (đơn vị hành chính mới) có sẵn tọa độ tâm trong bảng `wards`, nạp một lần từ dữ liệu bản đồ; thiếu tọa độ phường thì lúc seed điền tọa độ tâm Tỉnh/Thành (B4 bảng provinces, wards).
2. Khoảng cách ước lượng = khoảng cách đường chim bay (công thức haversine) × 1,3 để xấp xỉ đường bộ.
3. Không gọi dịch vụ bản đồ khi đặt hàng, nên không phụ thuộc mạng ngoài và không lưu tọa độ riêng của khách.

| Khoảng cách ước lượng | Vùng tương ứng (ví dụ) | Phí cơ bản (đơn ≤ 1 kg) |
| --- | --- | --- |
| ≤ 10 km | Các phường nội thành gần kho | 18.000 đ |
| 10–30 km | Phần còn lại của Hà Nội | 25.000 đ |
| 30–150 km | Các tỉnh lân cận Hà Nội | 30.000 đ |
| 150–500 km | Miền Bắc xa, Bắc Trung Bộ | 35.000 đ |
| > 500 km | Miền Trung, miền Nam | 40.000 đ |

Phụ phí cân nặng: +5.000 đ cho mỗi 0,5 kg vượt quá 1 kg (cân nặng đơn = tổng cân nặng sản phẩm, khai khi tạo sản phẩm).

Miễn phí ship:

- Đơn từ 499.000 đ và khoảng cách ≤ 30 km.
- Đơn từ 799.000 đ cho mọi khoảng cách.

Ví dụ: đơn 2 món nặng 1,4 kg, giá 420.000 đ, giao đi một tỉnh cách kho khoảng 80 km → phí = 30.000 + 5.000 = 35.000 đ.

Các mức phí, ngưỡng khoảng cách, hệ số 1,3 và ngưỡng miễn phí đều nằm trong cấu hình UC27 để Admin chỉnh.
