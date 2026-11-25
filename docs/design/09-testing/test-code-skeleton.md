Nguồn: 09-TESTING.md > B9 – Kế hoạch kiểm thử > Khung code test
## Khung code test

Mỗi service có thư mục test riêng, chia theo mức. Viết sẵn fixture và Fake để code xong là chạy được ngay.

```text
core_api/tests/
  unit/          # domain, service: StockPolicy, ShippingFeeCalculator, OrderStateMachine
  integration/   # api + db thật + repository; FakePaymentGateway cho payOS
  conftest.py    # fixture: db tạm, async client, factory user/product/order
ai_service/tests/
  unit/          # luật guardrail R1–R3, SizeAdvisor, ánh xạ tham số tool
  integration/   # api + schema ai; FakeCoreApiClient, FakeTryOnProvider
  eval/          # bộ ca đánh giá agent (B7): JSONL + runner đẩy Langfuse
web/e2e/         # Playwright: mua hàng, chat happy path
```

Ví dụ unit test cho phí ship (dùng parametrize cho giá trị biên ở mục 3):

```python
# core_api/tests/unit/test_shipping.py
import pytest
from core_api.domain.shipping import ShippingFeeCalculator

@pytest.mark.parametrize("km, kg, expected", [
    (8, 0.8, 18_000),
    (35, 1.6, 40_000),   # 30k + 2*5k vượt 1kg
    (600, 1.0, 40_000),
])
def test_phi_ship(km, kg, expected):
    assert ShippingFeeCalculator().fee(distance_km=km, weight_kg=kg) == expected

def test_freeship_tu_499k_trong_30km():
    calc = ShippingFeeCalculator()
    assert calc.fee(distance_km=25, weight_kg=1, order_total=520_000) == 0
```

Fixture chính: `db` (Postgres tạm qua testcontainers, migrate + rollback mỗi test), `client` (httpx AsyncClient), `make_user` / `make_product` / `make_order` (factory), `fake_payos` và `fake_core` (adapter giả để không gọi dịch vụ thật). ai-service dùng FakeCoreApiClient (đã nêu ở B7) để test agent không phụ thuộc core.

Tích hợp CI (GitHub Actions, mở rộng từ B3):

| Giai đoạn | Nội dung | Chặn merge? |
| --- | --- | --- |
| Lint & kiến trúc | ruff (C901 ngưỡng 10), import-linter | Có |
| Unit | pytest unit cả 2 service | Có |
| Integration | spin Postgres + Redis, pytest integration | Có |
| Contract | schemathesis đối chiếu OpenAPI (B5) | Có |
| E2E | Playwright happy path (nhánh main) | Cảnh báo |
| Đánh giá agent | chạy bộ eval, đẩy Langfuse | Thủ công / nightly |

