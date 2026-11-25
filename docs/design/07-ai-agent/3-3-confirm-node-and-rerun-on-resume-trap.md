Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 3. Graph > 3.3 Node `confirm` và bẫy "chạy lại node khi resume"
### 3.3 Node `confirm` và bẫy "chạy lại node khi resume"

Khi resume sau `interrupt`, LangGraph chạy lại node `confirm` **từ đầu**, không phải từ dòng `interrupt`. Vì vậy mọi việc đặt trước `interrupt` phải chạy lại nhiều lần mà không gây hậu quả. Nếu tạo dòng `pending_actions` ngay trong node, mỗi lần resume sẽ sinh thêm một dòng. Cách làm:

1. `confirm` chỉ tính toán, không ghi DB. `action_id = uuid5(conversation_id, tool_call_id)` nên lần nào tính cũng ra cùng một giá trị. `summary` sinh từ tên tool và tham số theo mẫu cố định (không gọi LLM), nên cũng luôn giống nhau.
2. `AgentRunner` thấy sự kiện interrupt thì ghi `PendingAction` với đúng `action_id` đó (ghi lại cũng không tạo dòng mới), rồi phát `action.pending`. Đây đúng là việc B6 đã giao cho `AgentRunner`.
3. Khi resume, `interrupt` trả về `{"decision": "approved" | "rejected" | "superseded"}` và `confirm` trả `Command` sang node tiếp theo.

```python
def confirm_node(state: AgentState, runtime: Runtime[AgentContext]) -> Command:
    call = state["messages"][-1].tool_calls[0]
    action_id = uuid5(runtime.context.conversation_id, call["id"])
    decision = interrupt({
        "action_id": str(action_id),
        "tool": call["name"],
        "args": call["args"],
        "summary": render_summary(call),  # mẫu cố định, không gọi LLM
    })["decision"]
    if decision == "approved":
        return Command(goto="run_write")
    text = "Người dùng đã từ chối." if decision == "rejected" else "Đã bỏ qua vì người dùng gửi yêu cầu khác."
    return Command(
        goto="agent" if decision == "rejected" else END,
        update={"messages": [ToolMessage(text, tool_call_id=call["id"])]},
    )
```

