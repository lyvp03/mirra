Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 5. Từ điển dữ liệu schema ai > 5.3 tryon\_jobs — job thử đồ và khung hình webcam (UC12–UC14, UC30, UC32, UC33)
### 5.3 tryon\_jobs — job thử đồ và khung hình webcam (UC12–UC14, UC30, UC32, UC33)

| Cột | Kiểu | Ràng buộc | Ý nghĩa |
| --- | --- | --- | --- |
| user\_id | uuid | ref users |  |
| kind | varchar(20) | CHECK IMAGE, VIDEO, SET\_IMAGE, WEBCAM\_SNAPSHOT |  |
| status | varchar(15) | CHECK PENDING, PROCESSING, COMPLETED, FAILED |  |
| photo\_id | uuid | NULL, FK user\_photos | Bắt buộc với IMAGE, SET\_IMAGE |
| source\_job\_id | uuid | NULL, FK tryon\_jobs | Bắt buộc với VIDEO: job ảnh nguồn |
| webcam\_session\_id | uuid | NULL, FK webcam\_sessions | Bắt buộc với WEBCAM\_SNAPSHOT |
| provider\_ref | varchar(100) | NULL, UNIQUE | Mã job bên provider, dùng khớp webhook |
| result\_key | varchar(255) | NULL | File kết quả trong bucket `tryon` |
| error | varchar(255) | NULL | Lý do FAILED |
| completed\_at | timestamptz | NULL |  |
| media\_deleted\_at | timestamptz | NULL | File kết quả đã xóa (UC14.2, UC30); dòng giữ cho thống kê |

Ràng buộc bảng: mỗi `kind` bắt buộc đúng một cột nguồn tương ứng (CHECK theo `kind`). Lượt đã dùng trong ngày không lưu: đếm job COMPLETED theo `user_id`, `kind` và ngày của `created_at`; job FAILED không tính nên tự động "hoàn lượt".

