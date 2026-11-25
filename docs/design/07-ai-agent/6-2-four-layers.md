Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 6. Guardrail > 6.2 Bốn lớp
### 6.2 Bốn lớp

Nguyên tắc: thứ gì quan trọng thì chặn bằng code, không trông vào việc LLM làm theo hướng dẫn.

| Lớp | Chặn | Cách làm | Đặt ở đâu |
| --- | --- | --- | --- |
| **0. Kiểm soát cứng** | Vượt quyền, thao tác ghi không xác nhận, vòng lặp, chi phí | Tool nạp theo vai trò; core kiểm quyền lại ở mọi API bằng JWT của người dùng; thao tác ghi qua `interrupt` với thẻ xác nhận sinh từ mẫu cố định; schema Pydantic cho tham số; hạn mức chat, 5 tool/lượt, `CostGuard` | B5, B6, mục 2–3 |
| **1. Đầu vào** | Tin quá dài, prompt injection trực tiếp, nội dung độc hại | Luật cố định rồi model phân loại (mục 6.3) | `AgentRunner`, trước graph |
| **2. Ngữ cảnh** | Prompt injection gián tiếp qua dữ liệu tool trả về | Chọn nguồn được đưa vào, bọc kết quả trong thẻ dữ liệu (mục 6.4) | Tool và system prompt |
| **3. Đầu ra** | Bịa giá, tồn (NFR10); lộ system prompt | Đối chiếu con số trong câu trả lời với dữ liệu tool (mục 6.5) | `AgentRunner`, sau graph |

Lớp 0 là lớp quyết định. Kể cả khi lớp 1–3 bị vượt qua, agent vẫn không làm được gì ngoài quyền của chính người đang chat. Mọi thao tác ghi còn phải được người đó bấm xác nhận trên một thẻ mô tả đúng tham số sẽ chạy. Thẻ này sinh bằng mẫu từ tham số thật, không phải do LLM viết, nên nội dung bị chèn vào không thể khiến thẻ nói một đằng làm một nẻo.

