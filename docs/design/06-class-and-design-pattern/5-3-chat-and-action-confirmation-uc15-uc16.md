Nguồn: 06-CLASS-AND-DESIGN-PATTERN.md > Mirra — B6: Thiết kế lớp và design pattern > 5. Sequence mức thiết kế > 5.3 Chat và xác nhận hành động (UC15, UC16)
### 5.3 Chat và xác nhận hành động (UC15, UC16)

```mermaid
sequenceDiagram
  participant R as ChatRouter
  participant C as ChatService
  participant L as ChatLimitPolicy
  participant AR as AgentRunner
  participant GR as Guardrail
  participant G as CompiledGraph
  participant T as CoreBackedTool
  participant K as CoreApiClient
  participant PA as PendingActionRepository
  participant AS as ActionService
  R->>C: send(conv_id, actor, content)
  C->>L: check(actor, used, limits)
  C->>C: save USER message
  C->>AR: stream(conv_id, actor, input)
  AR->>GR: check_input(content)
  alt blocked
    AR-->>R: event error GUARDRAIL_BLOCKED
  else allowed
    AR->>G: astream(input, thread_id=conv_id)
    G->>T: read tool call (search, track order)
    T->>K: request(GET, path, actor.token)
    K-->>T: data
    T-->>G: ToolResult
    G-->>AR: tokens, tool events, cards
    AR-->>R: token / tool.* / card.* events
    opt write tool
      G-->>AR: interrupt(tool, args)
      AR->>PA: add(PendingAction PENDING)
      AR-->>R: action.pending, stream ends
    end
    AR->>GR: check_output(final text)
    AR->>C: save ASSISTANT message with trace_id
    AR-->>R: message.end
  end
  Note over R,AS: Later the user taps Confirm
  R->>AS: confirm(action_id, actor)
  AS->>PA: get_pending(action_id)
  alt expired or decided
    AS-->>R: AppError ACTION_EXPIRED / ACTION_ALREADY_DECIDED
  else
    AS->>PA: mark CONFIRMED
    AS->>AR: stream(conv_id, actor, resume=confirm)
    AR->>G: resume(Command(resume=approved))
    G->>T: run(args, ctx with new token)
    T->>K: request(POST, path, actor.token)
    AR-->>R: action.result, tokens, message.end
  end
```

Phần gửi tin của sơ đồ này được chi tiết hóa ở [B7 mục 3.4](https://claude.ai/artifact/JqesBMTsjrfCLztNEuy1sk): guardrail đầu vào hai bước (luật rồi model phân loại), tự đóng thao tác đang chờ, `message.replace` khi đầu ra vi phạm. Phần bấm xác nhận giữ nguyên.

