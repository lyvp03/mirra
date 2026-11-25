Nguồn: 03-PACKAGE-COMPONENT-DEPLOYMENT.md > Mirra — B3: Package, Component, Deployment > 1. Quy ước và quyết định > 1.4 Quy tắc phụ thuộc
### 1.4 Quy tắc phụ thuộc

- Tầng trên chỉ gọi tầng ngay dưới hoặc `domain`; không gọi ngược lên.
- `services` chỉ biết interface của adapter, không biết SDK cụ thể (payOS, LangChain, MinIO…); adapter được inject lúc khởi động, đổi provider chỉ cần thêm adapter.
- `domain` không phụ thuộc framework (không import FastAPI, SQLAlchemy), để test độc lập.
- Worker dùng chung image và code với service tương ứng, chỉ khác lệnh khởi động.

