Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 3. Graph > 3.4 Một lượt chat, nhìn từ `AgentRunner`
### 3.4 Một lượt chat, nhìn từ `AgentRunner`

Sơ đồ này thay sequence "Chat và xác nhận" ở B6 mục 5.3 cho phần gửi tin; phần bấm xác nhận giữ nguyên như B6.

```mermaid
sequenceDiagram
  participant R as ChatRouter
  participant C as ChatService
  participant AR as AgentRunner
  participant GR as Guardrail
  participant G as CompiledGraph
  participant M as ChatMessageRepository
  R->>C: send(conv_id, actor, content)
  C->>C: closed after 7 idle days? then CONVERSATION_CLOSED
  C->>C: check chat limit, save USER message
  opt open PendingAction
    C->>AR: resume(decision superseded)
    AR->>G: Command(resume=superseded)
    G-->>AR: ToolMessage skipped, END
    AR-->>R: action.result EXPIRED
  end
  C->>AR: stream(conv_id, actor, content)
  AR->>GR: check_input(content) rules, then classifier
  alt blocked
    AR->>M: flag USER message
    AR-->>R: error GUARDRAIL_BLOCKED
  else allowed
    AR->>G: astream(messages, context)
    G-->>AR: tokens, tool updates, interrupt
    AR-->>R: token, tool.start, tool.end, card.*, action.pending
    AR->>GR: check_output(final text, tool data of the window)
    alt violation
      AR-->>R: message.replace(safe text)
      AR->>M: save ASSISTANT safe text, cards, guardrail_flag
    else ok
      AR->>M: save ASSISTANT text, cards, trace_id
    end
    AR-->>R: message.end
  end
```

Cách `AgentRunner` đổi luồng của graph thành sự kiện SSE (B5 mục 5.2). Graph chạy với `stream_mode=["messages", "updates"]`:

| Luồng của graph | Sự kiện SSE |
| --- | --- |
| `messages`: từng token của node `agent` (lọc theo `langgraph_node == "agent"`) | `token` |
| `updates`: node `agent` trả `AIMessage` có `tool_call` | `tool.start` |
| `updates`: node `tools` hoặc `run_write` trả `ToolMessage` | `tool.end`; có artifact thì thêm `card.products` / `card.outfit`; từ `run_write` thì thêm `action.result` |
| `updates` có khóa `__interrupt__` | Ghi `PendingAction`, phát `action.pending`, kết thúc luồng |

