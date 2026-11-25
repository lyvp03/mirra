Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 4. Tool > 4.5 `search_products`: tìm vector rồi lọc ở core
### 4.5 `search_products`: tìm vector rồi lọc ở core

1. **Có `query`:** embed câu tìm bằng `EmbeddingProvider`, lấy 30 sản phẩm gần nhất trong `search_documents` (chỉ `source_type = product` và `visible = true`).
2. Gọi core `GET /products?ids=<30 id>&category&color&size&price_min&price_max&in_stock=true`. Core lọc theo dữ liệu hiện tại và trả giá hiệu lực, tồn; tool giữ thứ tự theo độ gần về nghĩa.
3. Lấy `limit` món đầu, dựng `content` và `ProductsCard`.
4. **Không có `query`** (vd "đầm dưới 500k"): bỏ bước 1, gọi thẳng `GET /products` với bộ lọc.
5. **Không còn món nào:** `content` nói bộ lọc nào đang hẹp để agent gợi ý nới ra.

Vì sao chia như vậy: ai giữ phần hiểu câu chữ (embedding), core giữ phần sự thật (giá, tồn, hiển thị). Đúng ranh giới B3, và giá luôn là giá hiện tại dù index có trễ vài giây so với core. Chi phí embed câu tìm ghi qua `CostRecorder`.

Cần thêm vào B5: tham số `ids` (tối đa 30, phân cách bằng dấu phẩy) và `in_stock` cho `GET /products`.

