Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 6. Guardrail > 6.6 Lớp trong code
### 6.6 Lớp trong code

`Guardrail` của B6 được tách thành ba phần nhỏ, mỗi phần kiểm thử riêng:

- `InputRules`: R1–R3, thuần Python, không gọi mạng.
- `InputClassifier`: C1, gọi model qua `LLMProvider`.
- `OutputVerifier`: kiểm đầu ra ở mục 6.5, thuần Python.

`Guardrail.check_input(text)` gọi `InputRules` rồi `InputClassifier`. `Guardrail.check_output(text, tool_data)` gọi `OutputVerifier`; chữ ký này thêm tham số `tool_data` so với B6. Các giá trị của `chat_messages.guardrail_flag`: `INPUT_TOO_LONG`, `INPUT_INJECTION`, `INPUT_ABUSE`, `OUTPUT_UNVERIFIED_PRICE`, `OUTPUT_UNVERIFIED_STOCK`, `OUTPUT_PROMPT_LEAK`.

