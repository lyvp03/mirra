Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 5. Từ điển dữ liệu schema ai > 5.11 ai\_cost\_records — chi phí AI (UC26, UC28)
### 5.11 ai\_cost\_records — chi phí AI (UC26, UC28)

| Cột | Kiểu | Ràng buộc | Ý nghĩa |
| --- | --- | --- | --- |
| feature | varchar(20) | CHECK CHAT, GUARDRAIL, TRYON\_IMAGE, TRYON\_VIDEO, WEBCAM, PRODUCT\_DRAFT, EMBEDDING |  |
| provider | varchar(50) |  |  |
| units | integer | CHECK ≥ 0 | Token, giây hoặc số ảnh, theo `feature` |
| cost\_usd | numeric(10,4) | CHECK ≥ 0 |  |
| conversation\_id | uuid | NULL, FK conversations, ON DELETE SET NULL |  |
| tryon\_job\_id | uuid | NULL, FK tryon\_jobs, ON DELETE SET NULL |  |
| webcam\_session\_id | uuid | NULL, FK webcam\_sessions, ON DELETE SET NULL |  |

Ràng buộc bảng: tối đa một trong ba cột liên kết có giá trị (`num_nonnulls(...) <= 1`); bản ghi không liên kết dùng cho embedding và nháp sản phẩm.

