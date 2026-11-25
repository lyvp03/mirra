Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 8. Thay đổi so với B4–B6
## 8. Thay đổi so với B4–B6

Cả 8 mục của B7 đã được duyệt ngày 08/11. Mọi thay đổi dưới đây đã được áp dụng vào các tài liệu tương ứng trong cùng ngày.

| Tài liệu | Đã áp dụng | Từ mục |
| --- | --- | --- |
| Nguồn | Bảng tool theo vai trò (mục 2.2) theo 4.2, kèm dòng dẫn sang B7; mục mới 9.1 Đánh giá trợ lý AI; cách đo NFR10 trỏ sang 9.1 | 4, 7 |
| B1 | UC31 luồng 4a và activity diagram: "Thêm cả set vào giỏ" là thao tác trực tiếp của khách qua UC06.1, không qua UC16 | 4.6 |
| B2 | UC31: sequence và sơ đồ lớp thêm `CartController` cho thao tác thêm cả set; UC16: thẻ xác nhận chỉ đọc (bỏ `editedArgs`), thêm nhánh hết hạn 10 phút / gõ tin mới, `markRejected` | 2.6, 4.6 |
| B3 | Sơ đồ package: ai\_worker thêm checkpoint cleanup; ai\_service thêm `PromptBuilder`, ba phần của `Guardrail`, `SizeAdvisor`, `CheckpointCleanupJob`; package `eval` chỉ dùng khi kiểm thử | 3.6, 4, 6, 7 |
| B4 | `chat_messages.cards jsonb` (ERD, từ điển dữ liệu, bảng ngoại lệ JSONB); giá trị `guardrail_flag`; `GUARDRAIL` trong `ai_cost_records.feature` | 2.5, 6 |
| B5 | Setting `chat.action_ttl_minutes`, `chat.conversation_idle_days`; lỗi `CONVERSATION_CLOSED`, `AGENT_STEP_LIMIT`; sự kiện `message.replace`; `card.products` / `card.outfit` theo `ProductsCard` / `OutfitCard`; `GET /products` thêm `ids`, `in_stock`; mô tả `GET`/`POST .../messages`; file OpenAPI cập nhật và kiểm lại | 2, 3, 4, 6 |
| B6 | Sơ đồ lớp Assistant vẽ lại (PromptBuilder, Guardrail 3 phần, SizeAdvisor, CheckpointCleanupJob, `AgentRunner.resume`, `get_open`/`upsert`); ghi chú `AgentState`/`AgentContext`; sequence 5.3 dẫn sang B7 mục 3.4; 3 dòng mới ở bảng thay đổi | 2–6 |
| B7 | `OutfitCard` mang `outfit_id` + `sets` (khớp B5), thêm `OutfitItem` mức biến thể cho thử cả set | 4.3 |
