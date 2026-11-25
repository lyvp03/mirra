Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 5. Từ điển dữ liệu schema ai > 5.9 outfit\_suggestions — gợi ý phối đồ (UC31, UC32)
### 5.9 outfit\_suggestions — gợi ý phối đồ (UC31, UC32)

| Cột | Kiểu | Ràng buộc | Ý nghĩa |
| --- | --- | --- | --- |
| conversation\_id | uuid | FK conversations, ON DELETE CASCADE |  |
| anchor\_variant\_id | uuid | NULL, ref product\_variants | Món khách đang xem khi hỏi |
| sets | jsonb |  | 1–3 set, mỗi set gồm ID biến thể và lý do; bản chụp để vẽ lại thẻ trong chat |

