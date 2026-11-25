Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 2. State của agent > 2.3 Schema
### 2.3 Schema

```python
from dataclasses import dataclass
from typing import Annotated, Literal, TypedDict
from uuid import UUID

from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages


class PageContext(TypedDict):
    product_slug: str
    product_name: str  # lấy từ core lúc tạo hội thoại, để prompt dễ đọc


class AgentState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]  # giữ đủ; reducer nối thêm, không ghi đè
    page_context: PageContext | None  # None khi không mở từ trang sản phẩm


@dataclass(frozen=True)
class AgentContext:  # runtime context, KHÔNG được checkpoint
    conversation_id: UUID
    role: Literal["GUEST", "CUSTOMER", "STAFF", "ADMIN"]
    user_id: UUID | None
    guest_session_id: str | None
    access_token: str | None  # None với Guest
    trace_id: str
```

`AgentGraphFactory` dựng graph bằng `StateGraph(AgentState, context_schema=AgentContext)`. Node đọc context qua `runtime.context`, tool đọc qua runtime của tool. `AgentRunner` truyền context vào mỗi lần chạy:

```python
await graph.astream(
    {"messages": [HumanMessage(content)]},
    config={"configurable": {"thread_id": str(conversation_id)}},
    context=AgentContext(...),  # dựng từ ChatActor của request hiện tại
)
```

`page_context` được ghi một lần khi tạo hội thoại. `ChatService.create_conversation` lấy tên sản phẩm từ core theo `context.product_slug`, rồi gọi `graph.aupdate_state(config, {"page_context": ...})`. Slug không tồn tại hoặc sản phẩm đang ẩn thì để `None`.

