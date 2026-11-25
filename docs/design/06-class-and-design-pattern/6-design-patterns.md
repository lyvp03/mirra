Nguồn: 06-CLASS-AND-DESIGN-PATTERN.md > Mirra — B6: Thiết kế lớp và design pattern > 6. Design pattern
## 6. Design pattern

| Pattern | Áp dụng ở | Vấn đề giải quyết |
| --- | --- | --- |
| Adapter | `PayOSGateway`, `SmtpEmailSender`, `MinioStorage`, `LangfuseTraceStore`, các adapter của `TryOnProvider`, `RealtimeTryOnProvider`, `LLMProvider`, `EmbeddingProvider`, `PersonDetector` | SDK ngoài có giao diện riêng; service chỉ biết interface của Mirra nên đổi provider sau benchmark không sửa nghiệp vụ |
| Strategy | `ShippingFeeStrategy` (`DistanceTierStrategy`, sau này GHN); các hiện thực `TryOnProvider` hoán đổi theo cấu hình | Thuật toán tính phí hoặc provider thay được lúc chạy, `OrderService` không đổi |
| State (dạng bảng) | `OrderStateMachine` với `Order` là context | Hành vi hợp lệ của đơn phụ thuộc trạng thái và vai trò; gom mọi quy tắc vào một chỗ thay vì `if` rải rác trong 6 service method |
| Repository + Unit of Work | `Repository[T]` và các repository con; `UnitOfWork` | Tách truy vấn khỏi nghiệp vụ, mỗi lệnh ghi một transaction; test service bằng repository giả |
| Factory | `ProviderFactory` (chọn adapter theo biến môi trường), `AgentGraphFactory.build(role)` | Một chỗ duy nhất quyết định lớp cụ thể; graph của agent khác nhau theo vai trò (bộ tool) nhưng cùng cách dựng |
| Observer | `UnitOfWork.after_commit`; `EventPublisher` → các `StreamConsumer`; `Notifier` → handler SSE | Bên phát (core, worker) không biết ai lắng nghe; thêm bên nghe không sửa bên phát |
| Template Method | `StreamConsumer.run` + `handle`; `TryOnJobRunner.run` + `load_inputs`, `submit` | Khung xử lý cố định (đọc, ack, retry; nạp, gửi, ghi trạng thái), lớp con chỉ viết bước khác biệt |

