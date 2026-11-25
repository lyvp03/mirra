Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 2. State của agent > 2.4 Cửa sổ lịch sử gửi cho LLM
### 2.4 Cửa sổ lịch sử gửi cho LLM

Token phình lên chủ yếu vì kết quả tool: một lần tìm sản phẩm trả về khoảng 10 món, tức 2–3k token nếu để nguyên. Vì vậy có hai lớp giới hạn:

1. **Tool trả cho LLM bản rút gọn.** `ToolMessage.content` chỉ gồm tên, slug, giá, còn hàng hay không. Dữ liệu đầy đủ để vẽ thẻ nằm trong `ToolMessage.artifact` (kiểu `content_and_artifact` của LangChain) và không được gửi cho model.
2. **Node agent cắt cửa sổ trước khi gọi model.** Input của model = system prompt (vai trò + `page_context`) + cửa sổ tin gần nhất.

```python
window = trim_messages(
    state["messages"],
    max_tokens=HISTORY_TOKENS,  # 8000, cấu hình triển khai, xem lại sau đánh giá
    strategy="last",
    start_on="human",  # cửa sổ bắt đầu bằng tin của khách, không cắt đôi cặp tool_call / kết quả
    token_counter=count_tokens_approximately,  # không phụ thuộc tokenizer của provider
)
```

So sánh các cách đã cân nhắc:

|  | A. Giữ đủ, cắt khi gọi (chọn) | B. Tóm tắt phần cũ | C. Chỉ giữ N tin |
| --- | --- | --- | --- |
| Chi phí mỗi lượt (NFR13) | Có trần theo cửa sổ | Có trần, cộng một lần gọi LLM mỗi khi tóm tắt | Có trần |
| Độ trễ token đầu (NFR03) | Không tăng | Lượt phải tóm tắt chậm thêm, trừ khi chạy nền | Không tăng |
| Độ đúng (NFR10) | Tin ngoài cửa sổ thì gọi tool lại | Bản tóm tắt có thể giữ giá, tồn đã cũ hoặc làm rơi ID sản phẩm | Như A |
| Nhớ ngữ cảnh xa | Mất phần ngoài cửa sổ | Tốt nhất | Mất, và xóa hẳn |
| Công làm | Một hàm cắt | Thêm node, ngưỡng, prompt tóm tắt, kiểm thử chất lượng tóm tắt | Ít, nhưng phải xóa đúng cặp |

Hội thoại mua sắm có ngữ cảnh ngắn (hỏi món này, so món kia, thêm vào giỏ). Thứ dễ bị cắt mất nhất là sản phẩm đang xem, và cái này đã nằm riêng ở `page_context`. Nếu bộ đánh giá (mục 7) cho thấy agent quên ngữ cảnh trong hội thoại dài thì thêm B sau: chỉ cần một trường `summary` và một node, không phải làm lại.

