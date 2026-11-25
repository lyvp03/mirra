Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 5. Từ điển dữ liệu schema ai > 5.2 user\_photos — ảnh người dùng (UC12, UC14.2, UC30)
### 5.2 user\_photos — ảnh người dùng (UC12, UC14.2, UC30)

| Cột | Kiểu | Ràng buộc | Ý nghĩa |
| --- | --- | --- | --- |
| user\_id | uuid | ref users | Tối đa 3 ảnh chưa xóa, kiểm tra ở ứng dụng |
| object\_key | varchar(255) |  | Khóa trong bucket `tryon` |
| sha256 | char(64) |  | Dùng tra kết quả đã có (cache) |
| created\_at | timestamptz |  | Hạn xóa = created\_at + 30 ngày |
| deleted\_at | timestamptz | NULL | File đã xóa (người dùng hoặc UC30); dòng giữ lại vì job cũ tham chiếu |

