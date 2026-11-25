Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 4. Từ điển dữ liệu schema core > 4.3 provinces, wards — đơn vị hành chính (seed; UC04, UC07, BR11)
### 4.3 provinces, wards — đơn vị hành chính (seed; UC04, UC07, BR11)

| Bảng.cột | Kiểu | Ràng buộc | Ý nghĩa |
| --- | --- | --- | --- |
| provinces.code | varchar(5) | PK | Mã tỉnh/thành chính thức |
| provinces.name | varchar(100) |  |  |
| wards.code | varchar(10) | PK | Mã phường/xã chính thức |
| wards.province\_code | varchar(5) | FK provinces |  |
| wards.name | varchar(100) |  |  |
| wards.lat, wards.lng | double precision |  | Tọa độ tâm, dùng tính khoảng cách giao hàng; phường/xã thiếu tọa độ thì seed điền tọa độ tâm tỉnh (B1 mục 6.3), nên cột luôn có giá trị |

Hai bảng không có `id`, `created_at`.

