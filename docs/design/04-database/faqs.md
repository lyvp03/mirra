Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 4. Từ điển dữ liệu schema core > 4.17 faqs — FAQ và chính sách (UC21)
### 4.17 faqs — FAQ và chính sách (UC21)

| Cột | Kiểu | Ràng buộc | Ý nghĩa |
| --- | --- | --- | --- |
| question | varchar(300) |  | Tiêu đề với bài chính sách |
| answer | text |  |  |
| kind | varchar(10) | CHECK FAQ, POLICY |  |
| active | boolean | DEFAULT true |  |
| updated\_at | timestamptz |  |  |

Không có `created_at`.

