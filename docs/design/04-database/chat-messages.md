Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 5. Từ điển dữ liệu schema ai > 5.7 chat\_messages — tin nhắn hiển thị (UC15, UC28)
### 5.7 chat\_messages — tin nhắn hiển thị (UC15, UC28)

| Cột | Kiểu | Ràng buộc | Ý nghĩa |
| --- | --- | --- | --- |
| conversation\_id | uuid | FK conversations, ON DELETE CASCADE |  |
| role | varchar(10) | CHECK USER, ASSISTANT |  |
| content | text |  |  |
| trace\_id | varchar(64) | NULL | Trace Langfuse của lượt trả lời (UC28) |
| guardrail\_flag | varchar(30) | NULL | Lý do guardrail chặn hoặc thay câu trả lời; dùng lọc ở UC28. CHECK `INPUT_TOO_LONG`, `INPUT_INJECTION`, `INPUT_ABUSE`, `OUTPUT_UNVERIFIED_PRICE`, `OUTPUT_UNVERIFIED_STOCK`, `OUTPUT_PROMPT_LEAK` (B7 mục 6.6) |
| cards | jsonb | NULL | Danh sách thẻ sản phẩm / set của tin ASSISTANT theo thứ tự hiển thị, dạng `Card` ở B7 mục 4.3; để mở lại hội thoại vẫn thấy thẻ (UC15) |

Hạn mức chat đếm tin USER theo người dùng và ngày, hoặc theo phiên với Guest.

