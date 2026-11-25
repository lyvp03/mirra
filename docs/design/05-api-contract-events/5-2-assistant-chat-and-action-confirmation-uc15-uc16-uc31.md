Nguồn: 05-API-CONTRACT-EVENTS.md > Mirra — B5: API, contract, sự kiện > 5. Contract các luồng chính > 5.2 Chat với trợ lý và xác nhận hành động (UC15, UC16, UC31)
### 5.2 Chat với trợ lý và xác nhận hành động (UC15, UC16, UC31)

1. Guest xin `POST /ai/v1/chat/guest-sessions` một lần; người đã đăng nhập dùng access token.
2. `POST /ai/v1/chat/conversations` (có thể kèm `context.product_slug`), rồi gửi tin bằng `POST .../messages`. Response là SSE, web đọc bằng `fetch` + stream (không dùng `EventSource` vì cần POST và header).
3. Khi tool cần ghi dữ liệu, agent dừng (interrupt) và phát `action.pending`; web hiện thẻ xác nhận.
4. Người dùng bấm: `POST /ai/v1/chat/actions/{id}/confirm` hoặc `/reject`, kèm token hiện tại. Response là SSE tiếp tục câu trả lời.

Ví dụ một lượt gợi ý phối đồ:

```text
event: message.start
data: {"message_id": "m-01"}

event: tool.start
data: {"tool": "suggest_outfit", "label": "Đang phối đồ"}

event: tool.end
data: {"tool": "suggest_outfit", "ok": true}

event: card.outfit
data: {"outfit_id": "o-01", "sets": [{"index": 0, "reason": "...", "items": [{"variant_id": "...", "name": "Áo sơ mi lụa", "price": 359000, "in_stock": true, "try_on_enabled": true}]}]}

event: token
data: {"text": "Mình gợi ý 2 set..."}

event: message.end
data: {"message_id": "m-01"}
```

| Sự kiện | Dữ liệu | Web làm gì |
| --- | --- | --- |
| `message.start`, `message.end` | `message_id` | Mở, đóng bong bóng tin |
| `token` | `text` | Nối chữ |
| `message.replace` | `text` | Thay toàn bộ chữ của bong bóng bằng câu an toàn khi lớp kiểm đầu ra phát hiện vi phạm; giữ thẻ (B7 mục 6.5) |
| `tool.start`, `tool.end` | `tool`, `label`, `ok` | Hiện dòng trạng thái ngắn |
| `card.products` | `ProductsCard`: `items`, `action` (`view` / `open_tryon`), B7 mục 4.3 | Thẻ sản phẩm, nút thử đồ, nút webcam |
| `card.outfit` | `OutfitCard`: `outfit_id`, `sets` (1–3 set), B7 mục 4.3 | Thẻ set, nút thử cả set (UC32), nút webcam (UC33) |
| `action.pending` | `action_id, tool, summary, expires_at` | Thẻ xác nhận |
| `action.result` | `action_id, status, summary` | Cập nhật thẻ |
| `error` | `code, message` | Thông báo và đóng stream |

| Lỗi (trước khi mở stream) | HTTP | Khi nào |
| --- | --- | --- |
| `CHAT_LIMIT_REACHED` | 429 | Hết hạn mức tin theo vai trò; có `reset_at` |
| `ACTION_EXPIRED` | 409 | Xác nhận sau `expires_at` |
| `ACTION_ALREADY_DECIDED` | 409 | Bấm xác nhận hai lần |
| `GUEST_SESSION_INVALID` | 401 | Phiên Guest hết hạn |

Lỗi trong lúc stream (LLM lỗi, guardrail chặn) đi qua sự kiện `error` với `LLM_UNAVAILABLE` hoặc `GUARDRAIL_BLOCKED`.

