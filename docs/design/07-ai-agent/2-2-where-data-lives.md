Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 2. State của agent > 2.2 Dữ liệu nằm ở đâu
### 2.2 Dữ liệu nằm ở đâu

Có ba chỗ giữ dữ liệu của một hội thoại. **State** được checkpoint lưu lại. **Runtime context** truyền vào mỗi lần chạy graph và không được lưu. **Bảng DB** là nơi lưu bền để hiển thị và báo cáo.

| Dữ liệu | Nơi giữ | Vì sao |
| --- | --- | --- |
| Tin của khách, trợ lý, kết quả tool | State `messages` | Graph cần để chạy tiếp và resume sau `interrupt` |
| Lịch sử hiển thị (tin khách, tin trợ lý kèm thẻ) | Bảng `chat_messages` | Bền, không phụ thuộc checkpoint; Admin xem trace (UC28) |
| Sản phẩm đang xem | State `page_context` | Cần mỗi lượt, không được rơi khỏi cửa sổ |
| Số lần gọi tool trong lượt | Không lưu; đếm số `ToolMessage` từ tin cuối của khách | Tính được từ `messages`, lưu thêm là thừa và dễ lệch |
| Vai trò, `user_id` hoặc `guest_session_id`, `conversation_id` | Runtime context | Lấy từ JWT đã kiểm ở từng request, không tin giá trị cũ nằm trong checkpoint |
| Access token | Chỉ runtime context, **không bao giờ vào state** | Ghi vào checkpoint là để bí mật nằm trong DB; token sống 15 phút nên khi resume phải dùng token của request xác nhận |
| Thao tác chờ xác nhận | Bảng `pending_actions` (trạng thái, hạn) + payload của `interrupt` trong checkpoint | DB là nguồn đúng về trạng thái; checkpoint giữ chỗ graph dừng |
| Giá, tồn kho | Không lưu; mỗi lần cần thì gọi tool | NFR10 |
| `trace_id` của lượt | Runtime context → `chat_messages.trace_id` | Nối tin nhắn với trace Langfuse |

