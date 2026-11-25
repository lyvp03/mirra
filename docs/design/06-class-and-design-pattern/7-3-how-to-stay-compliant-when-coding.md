Nguồn: 06-CLASS-AND-DESIGN-PATTERN.md > Mirra — B6: Thiết kế lớp và design pattern > 7. Coupling và cohesion > 7.3 Cách giữ đúng khi code
### 7.3 Cách giữ đúng khi code

- `import-linter` chạy trong CI với các contract: tầng `api` → `services` → `domain`/`repositories` → `models` (không import ngược); `domain` cấm import `fastapi`, `sqlalchemy`, SDK provider; package của các component độc lập với nhau trừ các ngoại lệ ở 7.2.
- `ruff` bật quy tắc độ phức tạp (C901) với ngưỡng 10 cho mỗi hàm; hàm vượt ngưỡng tách bước ra domain.
- Test domain (`OrderStateMachine`, `StockPolicy`, `DistanceTierStrategy`, `PriceCalculator`, `WebcamBudgetPolicy`, `TryOnQuotaPolicy`, `SetRule`) không cần DB; service test bằng repository và adapter giả. Kế hoạch kiểm thử chi tiết để B9.

