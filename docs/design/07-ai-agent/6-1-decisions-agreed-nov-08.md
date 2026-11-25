Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 6. Guardrail > 6.1 Quyết định đã chốt (08/11)
### 6.1 Quyết định đã chốt (08/11)

| Vấn đề | Chốt |
| --- | --- |
| Số lớp | 4 lớp: kiểm soát cứng, đầu vào, ngữ cảnh, đầu ra |
| Lớp đầu vào | Luật cố định, rồi model phân loại, chạy **trước** agent |
| Nội dung đánh giá của khách | Agent không đọc; chỉ nhận điểm trung bình và số lượt |
| Lớp đầu ra | Stream bình thường, kiểm khi trả lời xong; vi phạm thì thay bằng câu an toàn |

