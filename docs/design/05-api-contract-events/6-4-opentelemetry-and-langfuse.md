Nguồn: 05-API-CONTRACT-EVENTS.md > Mirra — B5: API, contract, sự kiện > 6. Sự kiện > 6.4 OpenTelemetry và Langfuse
### 6.4 OpenTelemetry và Langfuse

- Mọi request mang header `traceparent` (W3C); web tạo ở trình duyệt, core và ai truyền tiếp khi gọi nhau và ghi vào `data` của Redis Streams để worker nối tiếp trace.
- Agent ghi trace lên Langfuse với `session_id` = `conversations.id`; `chat_messages.trace_id` lưu trace của từng lượt (UC28).

