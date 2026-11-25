# ai_service

## Architecture
- Layers: `api → services → repositories → models`.
- `domain` is pure: no I/O.
- External systems (core, LLM, try-on, storage) are reached only through `adapters/`.

## Agent
- `StateGraph` with 4 nodes (B7).
- English prompts live in `agent/prompts/`; never hard-code them in code.
- Write tools (`add_to_cart`, `update_order_status`) must `interrupt` and wait for user confirmation.
- At most 5 tool calls per turn. Parallel tool calls are disabled.

## Testing
- Unit tests never call a real LLM. Use `FakeCoreApiClient`, `FakeTryOnProvider` and a fake LLM.
