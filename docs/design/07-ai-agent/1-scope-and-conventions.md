Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 1. Phạm vi và quy ước
## 1. Phạm vi và quy ước

B7 thiết kế bên trong trợ lý AI: state, graph, tool, prompt, guardrail và cách đánh giá. Phần bao quanh đã có ở các bước trước:

- B5 mục 5: API chat, sự kiện SSE, xác nhận thao tác.
- B6 mục 4.1: `ChatService`, `ActionService`, `AgentRunner`, `AgentGraphFactory`, `ToolRegistry`, `Guardrail`.
- B4: các bảng `conversations`, `chat_messages`, `pending_actions`, `outfit_suggestions`.

Những điều đã chốt từ trước và B7 giữ nguyên:

- Một agent LangGraph, không multi-agent.
- Tool nạp theo vai trò và gọi core bằng JWT của người dùng.
- Mọi thao tác ghi phải xác nhận (BR17).
- Giá và tồn chỉ lấy từ tool (NFR10).

Về cách trình bày: code minh họa viết bằng Python với API của LangGraph từ bản 0.6 trở lên (có `context_schema` và `Runtime`). Sơ đồ vẽ bằng mermaid để vẽ lại trong Astah. Mỗi mục được viết sau khi đã khảo sát và chốt các điểm của mục đó.

