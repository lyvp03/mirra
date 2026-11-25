Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 2. State của agent > 2.8 Kích thước checkpoint
### 2.8 Kích thước checkpoint

Mỗi khi `messages` đổi, checkpointer Postgres lưu một phiên bản mới của **cả danh sách**, nên dung lượng của một hội thoại tăng nhanh hơn số tin.

Ước tính (chưa đo), giả định mỗi lượt khoảng 1k token sau khi đã rút gọn kết quả tool và khoảng 3 bước graph:

| Độ dài hội thoại | Dung lượng checkpoint (ước tính) |
| --- | --- |
| 10 lượt | Khoảng 0,7 MB |
| 50 lượt (trần của Customer trong một ngày) | Khoảng 15 MB |

Con số này không ảnh hưởng tới tốc độ, vì mỗi lần graph chỉ đọc checkpoint mới nhất. Nhưng nó là lý do phải dọn checkpoint cũ; quy tắc dọn chốt ở mục 3, phần vòng đời thread. Bảng `chat_messages` không bị ảnh hưởng bởi việc dọn này.

