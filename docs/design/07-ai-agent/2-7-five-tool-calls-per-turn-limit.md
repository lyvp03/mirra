Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 2. State của agent > 2.7 Giới hạn 5 lần gọi tool mỗi lượt
### 2.7 Giới hạn 5 lần gọi tool mỗi lượt

- Node agent đếm số `ToolMessage` kể từ `HumanMessage` cuối cùng. Không cần trường riêng trong state.
- Đếm đủ 5 thì gọi model **không gắn tool**, kèm một dòng nhắc: "Đã dùng hết lượt tra cứu, trả lời bằng thông tin đang có và nói rõ phần chưa tra được". Khách vẫn nhận được câu trả lời thay vì lỗi.
- Trường hợp model gọi nhiều tool song song trong một lần, mỗi tool tính một lần.
- `recursion_limit` của LangGraph là lưới an toàn cuối cùng. Giá trị cụ thể chốt cùng graph ở mục 3, khi đã biết số node.

