Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 5. Prompt > 5.1 Quyết định đã chốt (08/11)
### 5.1 Quyết định đã chốt (08/11)

| Vấn đề | Chốt |
| --- | --- |
| Ngôn ngữ của prompt | Tiếng Anh (system prompt, mô tả tool, prompt của model phân loại) |
| Ngôn ngữ trả lời | Theo ngôn ngữ tin gần nhất của khách, mặc định tiếng Việt; tên và mô tả sản phẩm giữ nguyên tiếng Việt |
| Xưng hô | "Mirra" – "bạn"; Staff/Admin cũng vậy nhưng giọng trung tính, ngắn gọn |
| Phạm vi | Mua sắm tại Mirra và tư vấn phối đồ chung; ngoài ra từ chối lịch sự và kéo về mua sắm |
| Lưu prompt | File trong repo, git quản lý; mỗi trace ghi `prompt_version` |

Vì sao viết prompt bằng tiếng Anh: cùng một nội dung, tiếng Việt tốn nhiều token hơn, mà system prompt bị gửi lại ở mọi lần gọi model. Các model cũng được huấn luyện làm theo hướng dẫn tiếng Anh nhiều nhất. Câu trả lời cho khách vẫn theo ngôn ngữ của khách.

