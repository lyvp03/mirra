Nguồn: 05-API-CONTRACT-EVENTS.md > Mirra — B5: API, contract, sự kiện > 8. File OpenAPI và điểm cần kiểm chứng > 8.1 File kèm theo
### 8.1 File kèm theo

`mirra-openapi.yaml` (OpenAPI 3.1.0, gửi kèm trong đoạn chat) gồm 18 path của các endpoint đánh dấu ✓ ở mục 3, 4 và 20 schema. File đã qua `openapi-spec-validator`. Cách dùng:

- Frontend sinh type TypeScript hoặc chạy mock server từ file này để làm giao diện trước khi backend xong.
- Khi code, FastAPI tự sinh spec đầy đủ; so spec sinh ra với file này để phát hiện lệch contract ở các luồng chính.

