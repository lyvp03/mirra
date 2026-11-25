Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 4. Tool > 4.3 Quy ước chung
### 4.3 Quy ước chung

- **Tham số dùng slug, màu, size, mã đơn 10 số; không dùng UUID.** Model hay chép sai chuỗi UUID dài, còn slug và mã đơn vừa ngắn vừa đã có sẵn trong `tool_data`. Tool tự đổi sang ID khi gọi core.
- **Kết quả gồm hai phần** (mục 2.4): `content` là bản rút gọn cho LLM, sẽ được bọc trong `tool_data` (mục 6.4); `card` là dữ liệu đầy đủ để web vẽ thẻ, nằm ở `ToolMessage.artifact`.
- **Tool gọi core bằng access token trong runtime context.** Guest không có token nên chỉ gọi được endpoint công khai. Core vẫn kiểm quyền ở mọi lần gọi (lớp 0).
- **Giới hạn độ dài kết quả:** tối đa 8 mục, mô tả mỗi sản phẩm cắt còn 200 ký tự, để mỗi `content` dưới khoảng 800 token.
- **Không trả nội dung đánh giá**, chỉ `rating_avg` và `rating_count` (mục 6.4).

```python
class ToolResult(BaseModel):
    content: str             # rút gọn cho LLM, sẽ được bọc trong <tool_data>
    card: Card | None = None  # đi vào ToolMessage.artifact, không gửi cho model


class ProductCardItem(BaseModel):
    product_id: UUID
    slug: str
    name: str
    thumbnail_url: str
    price: int               # giá hiệu lực lúc trả lời (VND)
    sale_price: int | None
    in_stock: bool
    try_on_enabled: bool     # chỉ Customer thấy nút Thử đồ; ảnh tham chiếu do hộp thử đồ tự lấy


class ProductsCard(BaseModel):
    type: Literal["products"] = "products"
    items: list[ProductCardItem]
    action: Literal["view", "open_tryon"] = "view"  # open_tryon: web mở hộp thử đồ ngay


class OutfitItem(BaseModel):  # mức biến thể, vì thử cả set (UC32) cần variant_id
    variant_id: UUID
    product_slug: str
    name: str
    color: str
    price: int
    image_url: str
    in_stock: bool
    try_on_enabled: bool


class OutfitSet(BaseModel):
    index: int
    reason: str
    items: list[OutfitItem]  # 1 trên + 1 dưới (BR20)


class OutfitCard(BaseModel):
    type: Literal["outfit"] = "outfit"
    outfit_id: UUID          # = outfit_suggestions.id
    sets: list[OutfitSet]    # 1–3 set


Card = Annotated[ProductsCard | OutfitCard, Field(discriminator="type")]
```

Sự kiện SSE `card.products` mang `ProductsCard`, `card.outfit` mang `OutfitCard`. Cột `chat_messages.cards` lưu `list[Card]`.

