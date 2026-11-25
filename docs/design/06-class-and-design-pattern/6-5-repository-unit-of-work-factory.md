Nguồn: 06-CLASS-AND-DESIGN-PATTERN.md > Mirra — B6: Thiết kế lớp và design pattern > 6. Design pattern > 6.5 Repository, Unit of Work, Factory
### 6.5 Repository, Unit of Work, Factory

- Repository trả model ORM, nhận tham số nghiệp vụ (`find_cached`, `find_expired_unpaid`), không lộ câu SQL ra service.
- `ProviderFactory` là composition root cho adapter, được gọi một lần lúc khởi động; FastAPI `Depends` lấy instance đã tạo để inject vào service.
- `AgentGraphFactory.build(role)` dựng graph LangGraph với bộ tool của vai trò, đệm graph đã biên dịch theo vai trò.

