Nguồn: 09-TESTING.md > B9 – Kế hoạch kiểm thử > Chiến lược & mức kiểm thử
## Chiến lược & mức kiểm thử

Kiểm thử theo kim tự tháp: nhiều unit test ở đáy, ít E2E ở đỉnh. Ưu tiên test tự động cho logic nghiệp vụ (lớp domain và service) vì đó là nơi rủi ro cao, thuần tính toán, dễ test và chạy nhanh. E2E chỉ phủ vài luồng sống còn (happy path) vì đắt và dễ vỡ.

| Mức | Phạm vi | Công cụ | Ví dụ ca |
| --- | --- | --- | --- |
| Unit | Hàm/lớp domain & service, không I/O: StockPolicy, ShippingFeeCalculator, OrderStateMachine, SizeAdvisor, luật guardrail R1–R3, OrderAccessPolicy | pytest + pytest-mock | Phí ship theo khoảng cách; chuyển trạng thái đơn hợp lệ |
| Integration | API + DB thật + repository trong một service; adapter ngoài dùng Fake | pytest + httpx AsyncClient + Postgres tạm (testcontainers); FakeGateway cho payOS/try-on | POST /orders trừ tồn đúng; webhook payOS idempotent |
| Contract | Giao tiếp giữa 2 service; đối chiếu OpenAPI B5 | pytest + schemathesis; FakeCoreApiClient | Tool ai add\_to\_cart gọi đúng contract core |
| E2E | Luồng người dùng qua web thật + 2 API | Playwright | Mua hàng Guest: duyệt → giỏ → checkout → VietQR (sandbox) |
| Chấp nhận / thủ công | Giao diện, try-on/webcam thực tế, trải nghiệm | Checklist thủ công theo B8 | Thử đồ bằng ảnh thật; responsive mobile |

Đánh giá AI agent (chất lượng trả lời, chọn tool, guardrail) và kiểm thử phi chức năng (tải, bảo mật) là hai nhánh riêng, không nằm trong kim tự tháp chức năng — xem mục 6 và 7. Kim tự tháp dưới đây tóm tắt tỉ trọng và phạm vi mỗi mức.

&#91;embedded content: 5 lop kiem thu, ty le ca test tu unit toi E2E\]

