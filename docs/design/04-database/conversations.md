Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 5. Từ điển dữ liệu schema ai > 5.6 conversations — hội thoại với trợ lý (UC15, UC28)
### 5.6 conversations — hội thoại với trợ lý (UC15, UC28)

| Cột | Kiểu | Ràng buộc | Ý nghĩa |
| --- | --- | --- | --- |
| user\_id | uuid | NULL, ref users |  |
| guest\_session\_id | varchar(64) | NULL | Mã phiên của Guest |
| actor\_role | varchar(10) | CHECK GUEST, CUSTOMER, STAFF, ADMIN | Vai trò lúc mở hội thoại, quyết định bộ tool |

Ràng buộc bảng: `CHECK (user_id IS NOT NULL OR guest_session_id IS NOT NULL)`. `id` cũng là mã luồng của LangGraph và mã session trên Langfuse.

