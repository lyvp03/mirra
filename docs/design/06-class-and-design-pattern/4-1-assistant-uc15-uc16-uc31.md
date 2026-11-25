Nguồn: 06-CLASS-AND-DESIGN-PATTERN.md > Mirra — B6: Thiết kế lớp và design pattern > 4. ai-service > 4.1 Assistant (UC15, UC16, UC31)
### 4.1 Assistant (UC15, UC16, UC31)

```mermaid
classDiagram
  class ChatService {
    <<service>>
    +create_guest_session(ip: str) str
    +create_conversation(actor: ChatActor, context: ChatContext) ConversationOut
    +list_messages(conversation_id: UUID, actor: ChatActor) list~MessageOut~
    +send(conversation_id: UUID, actor: ChatActor, content: str) AsyncIterator~ChatEvent~
  }
  class ActionService {
    <<service>>
    +confirm(action_id: UUID, actor: ChatActor) AsyncIterator~ChatEvent~
    +reject(action_id: UUID, actor: ChatActor) AsyncIterator~ChatEvent~
  }
  class OutfitService {
    <<service>>
    +suggest(req: OutfitRequest, actor: ChatActor) OutfitSuggestionOut
    +get(id: UUID, actor: ChatActor) OutfitSuggestionOut
  }
  class ChatLimitPolicy {
    <<domain>>
    +check(actor: ChatActor, used: int, limits: ChatLimits) None
  }
  class AgentRunner {
    +stream(thread_id: UUID, actor: ChatActor, input: AgentInput) AsyncIterator~ChatEvent~
    +resume(thread_id: UUID, actor: ChatActor, decision: Decision) AsyncIterator~ChatEvent~
  }
  class AgentGraphFactory {
    +build(role: Role) CompiledGraph
  }
  class PromptBuilder {
    +system_prompt(role: Role, page: PageContext | None, now: datetime, tools_exhausted: bool) str
    +version(role: Role) str
  }
  class ToolRegistry {
    +tools_for(role: Role) list~AgentTool~
  }
  class AccessPolicy {
    <<domain>>
    +allowed(role: Role, tool: str) bool
  }
  class Guardrail {
    +check_input(text: str) GuardrailResult
    +check_output(text: str, tool_data: list~str~) GuardrailResult
  }
  class InputRules {
    <<domain>>
    +check(text: str) GuardrailResult
  }
  class InputClassifier {
    +classify(text: str) GuardrailResult
  }
  class OutputVerifier {
    <<domain>>
    +verify(text: str, tool_data: list~str~, system_prompt: str) GuardrailResult
  }
  class AgentTool {
    <<abstract>>
    +name: str
    +requires_confirmation: bool
    +args_schema: type~BaseModel~
    +run(args: BaseModel, runtime: ToolRuntime)* ToolResult
  }
  class CoreBackedTool {
    <<abstract>>
    #core: CoreApiClient
  }
  class SuggestOutfitTool
  class RecommendSizeTool
  class SizeAdvisor {
    <<domain>>
    +recommend(chart: SizeChart, m: Measurements) SizeAdvice
  }
  class CoreApiClient {
    <<interface>>
    +request(method: str, path: str, token: str | None, json: dict) dict
    +internal(path: str, params: dict) dict
  }
  class LLMProvider {
    <<interface>>
    +chat_model(purpose: str) BaseChatModel
  }
  class CheckpointSaver {
    <<interface>>
  }
  class CheckpointCleanupJob {
    +run() None
  }
  class TraceStore {
    <<interface>>
    +callback(session_id: UUID, user_id: str) CallbackHandler
  }
  class ConversationRepository {
    <<repository>>
    +last_message_at(id: UUID) datetime | None
    +find_idle_before(before: datetime) list~UUID~
  }
  class ChatMessageRepository {
    <<repository>>
    +count_user_messages(actor: ChatActor, since: datetime) int
  }
  class PendingActionRepository {
    <<repository>>
    +get_pending(id: UUID) PendingAction | None
    +get_open(conversation_id: UUID) PendingAction | None
    +upsert(action: PendingAction) None
  }
  class OutfitSuggestionRepository {
    <<repository>>
  }
  class SearchIndexService {
    <<service>>
  }

  ChatService --> ChatLimitPolicy
  ChatService --> ConversationRepository
  ChatService --> ChatMessageRepository
  ChatService --> PendingActionRepository
  ChatService --> AgentRunner
  ActionService --> PendingActionRepository
  ActionService --> AgentRunner
  AgentRunner --> AgentGraphFactory
  AgentRunner --> Guardrail
  AgentRunner --> PendingActionRepository
  AgentRunner --> ChatMessageRepository
  AgentRunner --> TraceStore
  Guardrail --> InputRules
  Guardrail --> InputClassifier
  Guardrail --> OutputVerifier
  InputClassifier --> LLMProvider
  AgentGraphFactory --> ToolRegistry
  AgentGraphFactory --> PromptBuilder
  AgentGraphFactory --> LLMProvider
  AgentGraphFactory --> CheckpointSaver
  ToolRegistry --> AccessPolicy
  ToolRegistry o-- AgentTool
  AgentTool <|-- CoreBackedTool
  AgentTool <|-- SuggestOutfitTool
  CoreBackedTool <|-- RecommendSizeTool
  RecommendSizeTool --> SizeAdvisor
  CoreBackedTool --> CoreApiClient
  SuggestOutfitTool --> OutfitService
  OutfitService --> SearchIndexService
  OutfitService --> CoreApiClient
  OutfitService --> LLMProvider
  OutfitService --> OutfitSuggestionRepository
  CheckpointCleanupJob --> CheckpointSaver
  CheckpointCleanupJob --> ConversationRepository
  CheckpointCleanupJob --> PendingActionRepository
```

- `ChatActor` gồm `role`, `user_id` hoặc `guest_session_id`, và access token của request hiện tại. `AgentRunner` dựng từ đó `AgentContext` (runtime context của LangGraph, không được checkpoint); tool đọc token qua `ToolRuntime`. State của graph là `AgentState` gồm `messages` và `page_context` (B7 mục 2.3).
- `AgentRunner` là cầu nối giữa service và LangGraph: chạy graph với `thread_id` = `conversations.id`, đổi sự kiện của graph thành `ChatEvent` (B5 mục 5.2), gặp `interrupt` thì tạo `PendingAction` và phát `action.pending`; khi xác nhận thì resume graph với quyết định.
- Tool có `requires_confirmation = True` (thao tác ghi) luôn đi qua node `confirm` với `interrupt` trước khi chạy. 12 tool theo vai trò, graph 4 node, prompt và guardrail 4 lớp chi tiết ở B7 mục 3–6. `RecommendSizeTool` dùng domain `SizeAdvisor` so số đo với bảng size bằng code, không gọi LLM.
- `CheckpointSaver` là saver Postgres của LangGraph trên schema `ai`.
- `Guardrail` gồm `InputRules` (luật cố định), `InputClassifier` (model phân loại, timeout 1,5 giây) và `OutputVerifier` (đối chiếu số tiền, tồn với dữ liệu tool), B7 mục 6.
- `ChatService.send` gọi `PendingActionRepository.get_open`; còn thao tác chờ thì đánh EXPIRED và `AgentRunner.resume(superseded)` trước khi chạy lượt mới. Hội thoại không có tin quá `chat.conversation_idle_days` thì trả `CONVERSATION_CLOSED`.
- `CheckpointCleanupJob` chạy hằng đêm trong ai-worker: giữ bản checkpoint mới nhất của mỗi thread, xóa thread của hội thoại đã đóng và chuyển thao tác còn PENDING của chúng sang EXPIRED (B7 mục 3.6).

