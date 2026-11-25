Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 5. Từ điển dữ liệu schema ai > 5.4 tryon\_job\_items — món đồ trong job (UC12, UC32)
### 5.4 tryon\_job\_items — món đồ trong job (UC12, UC32)

| Cột | Kiểu | Ràng buộc | Ý nghĩa |
| --- | --- | --- | --- |
| job\_id | uuid | PK, FK tryon\_jobs, ON DELETE CASCADE |  |
| variant\_id | uuid | PK, ref product\_variants |  |

IMAGE có 1 dòng, SET\_IMAGE có 2 dòng; VIDEO lấy món từ job nguồn, WEBCAM\_SNAPSHOT từ phiên nên không có dòng.

