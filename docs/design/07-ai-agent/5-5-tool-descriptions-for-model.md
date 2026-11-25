Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 5. Prompt > 5.5 Mô tả tool cho model
### 5.5 Mô tả tool cho model

Mỗi tool có một `description` tiếng Anh gồm ba ý: tool làm gì, khi nào dùng, khi nào không dùng. Mô tả tham số kèm ví dụ giá trị tiếng Việt, vì đó là thứ khách sẽ gõ. Ví dụ:

```text
search_products: Find products in the Mirra catalog by a natural-language description and optional filters.
Use it when the user describes what they want or asks for options. Do not use it for one known product
(use get_product with its slug). Returns up to 8 products with current price and stock.
  query: the user's description in their words, e.g. "đầm đi tiệc nhẹ nhàng"
```

