Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 4. Tool > 4.4 Từng tool
### 4.4 Từng tool

| Tool | Tham số | Xử lý | `content` trả cho LLM |
| --- | --- | --- | --- |
| `search_products` | `query: str` (0–200 ký tự), `category`, `color`, `size`, `price_min`, `price_max`, `limit` (1–8, mặc định 5) | Xem mục 4.5 | Mỗi dòng: tên, slug, giá, giá khuyến mãi, màu còn hàng, điểm đánh giá |
| `get_product` | `slug` | Lấy chi tiết công khai | Tên, chất liệu, mô tả (200 ký tự), giá, bảng màu × size còn/hết, điểm đánh giá |
| `faq_policy` | `question: str` | Tìm vector top 3 trong nguồn FAQ | 3 cặp hỏi – đáp |
| `recommend_size` | `slug`, `height_cm`, `weight_kg`, `bust_cm?`, `waist_cm?`, `hip_cm?` | `SizeAdvisor` so số đo với `size_charts.measurements` bằng code, không dùng LLM; báo luôn size đó còn hàng màu nào | Size đề xuất, lý do theo số đo, tình trạng hàng; thiếu số đo bắt buộc thì nói cần thêm gì |
| `suggest_outfit` | `slug`, `color`, `occasion?`, `budget_max?` | `OutfitService.suggest` (B6), 1–3 set theo BR20 | Tóm tắt từng set: tên món, giá, tổng |
| `start_tryon` | `slug`, `color` | Kiểm sản phẩm bật thử đồ và màu có ảnh tham chiếu thử đồ (BR15); phụ kiện không thử được | "Đã mở hộp thử đồ" hoặc lý do không thử được |
| `get_my_orders` | `order_code?` | Không có mã thì lấy 5 đơn gần nhất; có mã thì lấy chi tiết | Mã, ngày, trạng thái, tổng tiền, trạng thái thanh toán, mã vận đơn |
| `add_to_cart` | `slug`, `color`, `size`, `quantity` (1–10) | Mục 4.6 | "Đã thêm…, trong giỏ có N" hoặc lỗi từ core |
| `list_orders` | `status?`, `q?` (mã đơn, sđt, email), `limit` (1–10) | Lọc đơn | Mã, khách, trạng thái, tổng, phương thức thanh toán, đã gọi xác nhận chưa |
| `update_order_status` | `order_code`, `action`, `tracking_no?`, `reason?`, `phone_checked?` | Mục 4.6 | Trạng thái mới hoặc lỗi từ core |
| `low_stock` | `limit` (1–20) | SKU có tồn ≤ ngưỡng cảnh báo | SKU, tên, màu, size, tồn |
| `sales_report` | `from_date`, `to_date` (tối đa 92 ngày) | Báo cáo tổng hợp | Doanh thu, số đơn theo trạng thái, top 5 sản phẩm |

Ví dụ schema đầy đủ của một tool. Các tool khác viết cùng kiểu; mô tả cho model theo quy ước ở mục 5.

```python
class SearchProductsArgs(BaseModel):
    query: str = Field("", max_length=200, description="Mô tả món đồ bằng lời của khách, vd 'đầm đi tiệc nhẹ nhàng'")
    category: str | None = Field(None, description="Slug danh mục, vd 'dam-vay-lien', 'ao-so-mi-ao-kieu'")
    color: str | None = None
    size: str | None = None
    price_min: int | None = Field(None, ge=0)
    price_max: int | None = Field(None, ge=0)
    limit: int = Field(5, ge=1, le=8)


class SearchProductsTool(CoreBackedTool):
    name = "search_products"
    requires_confirmation = False
    args_schema = SearchProductsArgs
```

