Nguồn: 06-CLASS-AND-DESIGN-PATTERN.md > Mirra — B6: Thiết kế lớp và design pattern > 3. core-api > 3.4 Administration (UC26, UC27)
### 3.4 Administration (UC26, UC27)

```mermaid
classDiagram
  class ReportService {
    <<service>>
    +summary(start: date, end: date) ReportSummary
    +export_csv(start: date, end: date) bytes
  }
  class SettingsService {
    <<service>>
    +list_all() list~SettingOut~
    +public() dict
    +update(key: str, value: Any, actor: CurrentUser) SettingOut
    +history(key: str) list~SettingHistoryOut~
  }
  class SettingSchemaRegistry {
    <<domain>>
    +validate(key: str, value: Any) Any
    +is_public(key: str) bool
  }
  class DbSettingsProvider {
    -cache: dict
    +get(key: str) Any
    +public() dict
  }
  class SettingsProvider {
    <<interface>>
  }
  class AiUsageClient {
    <<interface>>
    +usage_summary(start: date, end: date) AiUsage
  }
  class HttpAiUsageClient
  class OrderRepository {
    <<repository>>
    +revenue_by_status(start: date, end: date) list~StatusRevenue~
    +top_variants(start: date, end: date, limit: int) list~TopVariant~
  }
  class SettingRepository {
    <<repository>>
  }
  class SettingHistoryRepository {
    <<repository>>
  }
  class EventPublisher {
    <<interface>>
  }

  ReportService --> OrderRepository
  ReportService --> AiUsageClient
  SettingsService --> SettingRepository
  SettingsService --> SettingHistoryRepository
  SettingsService --> SettingSchemaRegistry
  SettingsService --> EventPublisher
  SettingsProvider <|.. DbSettingsProvider
  DbSettingsProvider --> SettingRepository
  AiUsageClient <|.. HttpAiUsageClient
```

- `SettingSchemaRegistry` chứa schema Pydantic của từng khóa ở B5 mục 7.2 và cờ công khai.
- `ReportService` đọc `OrderRepository` của Ordering bằng truy vấn tổng hợp chỉ đọc; là ngoại lệ thứ hai được chấp nhận ở mục 7 (báo cáo cần đọc chéo).
- Nếu ai-service không trả lời, báo cáo vẫn trả phần số liệu bán hàng và đánh dấu phần AI là không có.

