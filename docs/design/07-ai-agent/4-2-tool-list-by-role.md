Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 4. Tool > 4.2 Danh sách tool theo vai trò
### 4.2 Danh sách tool theo vai trò

| Tool | Guest | Customer | Staff | Admin | Ghi? | Gọi tới | Thẻ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `search_products` | ✓ | ✓ | ✓ | ✓ | Không | `SearchIndexService` (ai) + `GET /products` (core) | products |
| `get_product` | ✓ | ✓ | ✓ | ✓ | Không | `GET /products/{slug}` | products |
| `faq_policy` | ✓ | ✓ | ✓ | ✓ | Không | `SearchIndexService` (ai), nguồn FAQ | — |
| `recommend_size` | ✓ | ✓ |  |  | Không | `GET /products/{slug}` + `SizeAdvisor` (ai) | — |
| `suggest_outfit` |  | ✓ |  |  | Không (\*) | `OutfitService` (ai) | outfit |
| `start_tryon` |  | ✓ |  |  | Không | `GET /products/{slug}` | products, mở hộp thử đồ |
| `get_my_orders` |  | ✓ |  |  | Không | `GET /orders`, `GET /orders/{code}` | — |
| `add_to_cart` |  | ✓ |  |  | **Có** | `GET /cart` + `PUT /cart/items/{variant_id}` | — |
| `list_orders` |  |  | ✓ | ✓ | Không | `GET /admin/orders` | — |
| `update_order_status` |  |  | ✓ | ✓ | **Có** | `POST /admin/orders/{id}/{action}` | — |
| `low_stock` |  |  | ✓ | ✓ | Không | `GET /admin/inventory` (hàng sắp hết) | — |
| `sales_report` |  |  |  | ✓ | Không | `GET /admin/reports/summary` | — |
| **Số tool** | 4 | 8 | 6 | 7 |  |  |  |

(\*) `suggest_outfit` có ghi một dòng `outfit_suggestions` ở schema ai, nhưng đây là dữ liệu nội bộ của trợ lý, không đổi gì của khách, nên không cần xác nhận.

So với tài liệu nguồn, có ba thay đổi:

- **Thêm `get_product`.** Khách thường hỏi tiếp về đúng một món ("màu kem còn size M không?", "chất gì?"), và sản phẩm trong `page_context` cũng cần một tool để lấy chi tiết. Nếu chỉ có `search_products`, agent phải tìm lại bằng câu chữ, kết quả dễ lệch.
- **Thêm `add_to_cart`** theo quyết định ở 4.1.
- **Bỏ `draft_product_from_image`** khỏi chat theo quyết định ở 4.1.

