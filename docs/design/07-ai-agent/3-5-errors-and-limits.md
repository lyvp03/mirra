Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 3. Graph > 3.5 Lỗi và giới hạn
### 3.5 Lỗi và giới hạn

| Tình huống | Xử lý |
| --- | --- |
| Core trả 4xx kèm `code` (vd hết hàng, không tìm thấy, không đủ quyền) | `ToolMessage` "Lỗi `<code>`: `<detail>`", agent giải thích cho khách. Không thử lại |
| Core 5xx hoặc quá thời gian | Tool đọc thử lại một lần rồi trả `ToolMessage` "hệ thống tạm không tra được". Tool ghi **không tự thử lại**, vì có thể lần đầu đã ghi xong |
| Tham số model sinh ra sai schema | `ToolMessage` mô tả lỗi schema; model sửa ở lần gọi sau (vẫn tính vào 5 lần) |
| Provider LLM lỗi | Thử lại một lần (`max_retries=1`), rồi phát `error` `LLM_UNAVAILABLE`. Tin của khách vẫn nằm trong state; lượt sau chạy bình thường |
| Chạm `recursion_limit` | Đặt **20**: mỗi vòng tool tốn tối đa 3 bước (`agent` → `confirm` → `run_write`), 5 vòng và 1 lần trả lời cuối là 16 bước, cộng dư. Chạm tới nghĩa là có lỗi logic, phát `error` `AGENT_STEP_LIMIT` |

