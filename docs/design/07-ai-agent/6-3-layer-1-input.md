Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 6. Guardrail > 6.3 Lớp 1: đầu vào
### 6.3 Lớp 1: đầu vào

Chạy theo thứ tự; bước nào chặn thì dừng ở đó.

| Bước | Kiểm | Kết quả khi chặn |
| --- | --- | --- |
| R1 | Tin dài quá 2.000 ký tự | `INPUT_TOO_LONG` |
| R2 | Mẫu injection phổ biến, tiếng Việt và Anh: "bỏ qua (mọi/các) hướng dẫn", "ignore (all/previous) instructions", "system prompt", "you are now", "developer mode"… Danh sách nằm trong file cấu hình, bổ sung dần từ bộ đánh giá | `INPUT_INJECTION` |
| R3 | Cố giả thẻ dữ liệu của lớp 2 (`<tool_data`, `</tool_data>`) | `INPUT_INJECTION` |
| C1 | Model phân loại nhỏ (`LLMProvider.chat_model("guardrail")`), trả về có cấu trúc `{label: SAFE / INJECTION / ABUSE, reason}` | `INPUT_INJECTION` hoặc `INPUT_ABUSE` |

Chỉ INJECTION và ABUSE bị chặn. Câu hỏi lạc đề (hỏi thời tiết, nhờ làm bài tập) không bị chặn ở đây; agent tự từ chối lịch sự theo system prompt, như vậy thân thiện hơn một thông báo lỗi.

**Ngân sách độ trễ (NFR03, token đầu dưới 3 giây):** C1 có timeout 1,5 giây, phần còn lại dành cho agent ra token đầu. Quá timeout hoặc model phân loại lỗi thì **cho qua** với kết quả của R1–R3, ghi cờ `CLASSIFIER_SKIPPED` vào trace. Không chặn trong trường hợp này vì lớp 0 vẫn giữ hậu quả, còn chặn thì chat ngừng hoạt động mỗi khi provider chậm.

Chi phí của C1 ghi qua `CostRecorder` với feature `GUARDRAIL`. C1 thuộc phần chat, nên vẫn chạy khi chạm trần chi phí tháng (Q4 ở tài liệu rà soát).

Khi bị chặn:

- Tin USER vẫn được lưu kèm `guardrail_flag` để Admin xem lại (UC28), và vẫn tính vào hạn mức chat để không dò thử miễn phí.
- State không đổi: tin bị chặn không vào `messages`.
- Web nhận `error` `GUARDRAIL_BLOCKED` kèm câu nhắc ngắn.

