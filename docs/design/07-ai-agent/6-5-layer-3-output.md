Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 6. Guardrail > 6.5 Lớp 3: đầu ra
### 6.5 Lớp 3: đầu ra

Khi agent trả lời xong, `Guardrail.check_output(text, tool_data)` kiểm ba điều. `tool_data` là mọi kết quả tool nằm trong cửa sổ đã gửi cho model.

| Kiểm | Cách làm | Cờ khi vi phạm |
| --- | --- | --- |
| Số tiền | Mọi số tiền trong câu trả lời (459.000đ, 459k, 459,000 VND…) sau khi chuẩn hóa phải có trong `tool_data`: giá, giá khuyến mãi, phí ship, tổng đơn | `OUTPUT_UNVERIFIED_PRICE` |
| Số lượng tồn | Cụm "còn N" phải khớp tồn trong `tool_data` | `OUTPUT_UNVERIFIED_STOCK` |
| Lộ prompt | Câu trả lời chứa một đoạn từ 40 ký tự trở lên trùng với system prompt | `OUTPUT_PROMPT_LEAK` |

Khi vi phạm:

1. Phát sự kiện SSE mới `message.replace` kèm câu an toàn, ví dụ "Mình chưa chắc chắn về thông tin này. Bạn xem giá và tình trạng hàng chính xác ở thẻ hoặc trang sản phẩm nhé." Web thay bọt thoại bằng câu này. Thẻ vẫn giữ, vì dữ liệu thẻ lấy thẳng từ tool.
2. Lưu tin ASSISTANT bằng câu an toàn kèm `guardrail_flag`. Câu gốc chỉ còn trong trace Langfuse để Admin xem (UC28).
3. Thay cả `AIMessage` trong state bằng câu an toàn (`aupdate_state`, cùng `id` nên `add_messages` ghi đè), để các lượt sau model không nhìn thấy và lặp lại con số sai của chính nó.

Rủi ro biết trước: con số do agent tự tính (vd "rẻ hơn 50k") không có trong `tool_data` nên sẽ bị chặn nhầm. System prompt dặn không tự tính tiền; tỉ lệ chặn nhầm được đo ở mục 7.

