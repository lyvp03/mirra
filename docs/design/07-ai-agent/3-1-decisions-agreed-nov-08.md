Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 3. Graph > 3.1 Quyết định đã chốt (08/11)
### 3.1 Quyết định đã chốt (08/11)

| Vấn đề | Chốt | Lý do ngắn |
| --- | --- | --- |
| Cách dựng | `StateGraph` tự khai báo, 4 node | Mỗi node vẽ và giải thích được; giới hạn tool và luật xác nhận nằm rõ trong graph thay vì trong middleware dựng sẵn |
| Gọi tool song song | Tắt: mỗi lần model gọi một tool (`parallel_tool_calls=False`) | Đơn giản: mỗi bước đúng một tool, không có trường hợp đọc và ghi lẫn nhau |
| Guardrail | Lớp đầu vào và đầu ra nằm ngoài graph, trong `AgentRunner` (mục 6) | Tin bị chặn không lọt vào state |
| Vòng đời hội thoại | 7 ngày không có tin mới thì đóng (chỉ xem lại) và xóa checkpoint; hằng đêm xóa các bản checkpoint cũ, giữ bản mới nhất | Checkpoint gọn (mục 2.8); lịch sử hiển thị vẫn còn ở `chat_messages` |

