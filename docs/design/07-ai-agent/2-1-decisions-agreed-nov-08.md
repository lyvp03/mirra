Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 2. State của agent > 2.1 Quyết định đã chốt (08/11)
### 2.1 Quyết định đã chốt (08/11)

| Vấn đề | Chốt | Lý do ngắn |
| --- | --- | --- |
| Lịch sử hội thoại | Giữ đủ trong state, khi gọi LLM chỉ gửi cửa sổ gần nhất (khoảng 8k token) | Chi phí và độ trễ có trần, không tốn thêm LLM, không có bản tóm tắt giữ giá cũ (mục 2.4) |
| Thẻ sản phẩm, thẻ set | Lưu kèm tin trả lời trong `chat_messages.cards` | Mở lại hội thoại thấy đúng như lúc chat, không phụ thuộc checkpoint |
| Nhớ giữa các hội thoại | Không; mỗi hội thoại độc lập, cần gì thì tool đọc từ core | Gọn phạm vi, không thêm dữ liệu cá nhân phải xin đồng ý (NFR09) |
| Sản phẩm đang xem | Trường `page_context` trong state, chèn vào system prompt mỗi lượt | Không bị cắt khỏi cửa sổ lịch sử |
| Hạn của thao tác chờ xác nhận | 10 phút | Đủ để đọc và bấm, tham số ít bị cũ |
| Gõ tin mới khi đang chờ xác nhận | Tự hủy thao tác cũ (EXPIRED) rồi xử lý tin mới | Giống cách người dùng hay làm ("thôi, đổi size M"); không bao giờ coi tin nhắn là xác nhận (BR17) |
| Số lần gọi tool mỗi lượt | Tối đa 5; quá thì trả lời bằng thông tin đang có | Chặn vòng lặp, giữ chi phí; khách thấy câu trả lời thay vì lỗi |

