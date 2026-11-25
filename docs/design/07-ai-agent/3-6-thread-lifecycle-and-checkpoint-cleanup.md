Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 3. Graph > 3.6 Vòng đời thread và dọn checkpoint
### 3.6 Vòng đời thread và dọn checkpoint

- `thread_id = conversations.id`, như B6.
- **Đóng hội thoại:** tin cuối trong `chat_messages` cũ hơn `chat.conversation_idle_days` ngày (setting mới, mặc định 7) thì hội thoại coi là đã đóng. Trạng thái này tính từ thời gian tin cuối, không cần thêm cột. Gửi tin vào hội thoại đã đóng thì nhận `CONVERSATION_CLOSED` (409), web mở hội thoại mới. Xem lại lịch sử và thẻ vẫn được.
- **`CheckpointCleanupJob`** chạy hằng đêm trong ai-worker:
  1. Với mỗi thread, xóa mọi checkpoint trừ bản mới nhất, kèm blob và write của chúng. Bản mới nhất đủ để chạy tiếp và resume.
  2. Thread của hội thoại đã đóng thì xóa hẳn (`adelete_thread`); `PendingAction` còn PENDING của hội thoại đó chuyển EXPIRED.
- **Cái giá:** mất khả năng "tua lại" state cũ của LangGraph. Mirra không dùng tính năng này; để xem lại từng lượt đã có trace trên Langfuse và `chat_messages`.
- Job chạy ban đêm và chỉ xóa bản cũ hơn bản mới nhất, nên không đụng tới lượt đang chạy.

Nếu trễ tiến độ, `CheckpointCleanupJob` là mục đầu tiên trong danh sách cắt (mục 11 tài liệu nguồn): thay bằng script SQL cùng logic, chạy tay hằng tuần.

