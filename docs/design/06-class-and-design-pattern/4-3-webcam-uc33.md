Nguồn: 06-CLASS-AND-DESIGN-PATTERN.md > Mirra — B6: Thiết kế lớp và design pattern > 4. ai-service > 4.3 Webcam (UC33)
### 4.3 Webcam (UC33)

```mermaid
classDiagram
  class WebcamService {
    <<service>>
    +availability(user: CurrentUser) AvailabilityOut
    +open_session(user: CurrentUser, variant_ids: list~UUID~) WebcamSessionOut
    +end_session(user: CurrentUser, id: UUID, used_seconds: int) WebcamSessionOut
    +save_snapshot(user: CurrentUser, id: UUID, frame: Upload) TryOnJobOut
    +sweep_stale(now: datetime) int
  }
  class WebcamBudgetPolicy {
    <<domain>>
    +can_open(sessions_today: int, used_total: int, open_reserved: int, limits: WebcamLimits) Decision
    +charge(used_seconds: int, max_seconds: int) int
  }
  class WebcamSweepJob {
    +run() None
  }
  class RealtimeTryOnProvider {
    <<interface>>
    +create_session(reference_image: bytes, max_seconds: int) ProviderSession
    +stop_session(ref: str) None
    +used_seconds(ref: str) int | None
  }
  class WebcamSessionRepository {
    <<repository>>
    +count_today(user_id: UUID, day_start: datetime) int
    +sum_used() int
    +sum_open_reserved() int
    +find_open_before(before: datetime) list~WebcamSession~
  }
  class OutfitComposer {
    <<domain>>
  }
  class SetRule {
    <<domain>>
  }
  class CoreApiClient {
    <<interface>>
  }
  class TryOnJobRepository {
    <<repository>>
  }
  class ObjectStorage {
    <<interface>>
  }
  class CostRecorder {
    <<service>>
  }
  class CostGuard {
    <<service>>
  }

  WebcamService --> WebcamBudgetPolicy
  WebcamService --> WebcamSessionRepository
  WebcamService --> RealtimeTryOnProvider
  WebcamService --> OutfitComposer
  WebcamService --> SetRule
  WebcamService --> CoreApiClient
  WebcamService --> TryOnJobRepository
  WebcamService --> ObjectStorage
  WebcamService --> CostRecorder
  WebcamService --> CostGuard
  WebcamSweepJob --> WebcamService
```

- `open_session` chạy trong một `UnitOfWork` có `advisory_lock(WEBCAM_BUDGET_LOCK)`: đếm phiên hôm nay, tổng giây đã dùng, tổng giây đang giữ → `WebcamBudgetPolicy.can_open` → tạo phiên OPEN → commit, rồi mới gọi provider. Provider lỗi thì đóng phiên với `used_seconds = 0` (trả lại ngân sách).
- `WebcamSweepJob` chạy mỗi phút: phiên OPEN quá `max_seconds` + thời gian ân hạn thì gọi `stop_session`, đóng EXPIRED và tính đủ `max_seconds`.

