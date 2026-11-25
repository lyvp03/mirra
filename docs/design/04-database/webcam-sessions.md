Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 5. Từ điển dữ liệu schema ai > 5.5 webcam\_sessions — phiên thử qua webcam (UC33, BR21)
### 5.5 webcam\_sessions — phiên thử qua webcam (UC33, BR21)

| Cột | Kiểu | Ràng buộc | Ý nghĩa |
| --- | --- | --- | --- |
| user\_id | uuid | ref users |  |
| target | jsonb |  | Món hoặc set được thử và ảnh tham chiếu đã gửi provider; chỉ đọc nguyên khối |
| provider\_session\_ref | varchar(100) | NULL |  |
| max\_seconds | smallint | CHECK > 0 | Thời lượng tối đa lúc mở phiên (20) |
| used\_seconds | smallint | NULL; CHECK 0 ≤ used\_seconds ≤ max\_seconds | Số giây tính phí khi đóng; bằng max\_seconds khi job dọn phiên đóng hộ |
| status | varchar(10) | CHECK OPEN, CLOSED, EXPIRED |  |
| started\_at | timestamptz | DEFAULT now() |  |
| ended\_at | timestamptz | NULL |  |

Không có bảng ngân sách riêng. Giới hạn 1 phiên/ngày đếm theo `started_at`; ngân sách toàn hệ thống = tổng `used_seconds` của phiên đã đóng cộng tổng `max_seconds` của phiên OPEN, so với trần trong `settings` (250 giây). Phép kiểm tra và tạo phiên chạy trong một transaction có khóa advisory để hai người không cùng giữ chỗ vượt trần.

