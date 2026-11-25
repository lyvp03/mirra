Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 7. Kế hoạch đánh giá agent > 7.3 Cấu trúc một ca test
### 7.3 Cấu trúc một ca test

Mỗi ca là một dòng JSONL. Model sinh ca phải xuất đúng cấu trúc này; harness đọc vào bằng Pydantic, ca nào sai cấu trúc bị loại.

```yaml
id: CUS-WRITE-004               # <VAI TRÒ>-<NHÓM>-<số>
role: CUSTOMER                  # GUEST | CUSTOMER | STAFF | ADMIN
category: write                 # normal | multi_turn | write | attack | out_of_scope | missing_info
subtype: null                   # với attack: xem mục 7.4
fixture_user: cus_lan           # người dùng giả trong fixture; null với Guest
page_context: {product_slug: ao-so-mi-lua-cotton}   # hoặc null
turns:
  - user: "lấy mình cái này màu kem size M nhé"
    decision: approved          # chỉ có khi lượt này sinh thẻ xác nhận: approved | rejected | superseded
expect:
  tools: [get_product, add_to_cart]
  tool_args:
    add_to_cart: {slug: ao-so-mi-lua-cotton, color: kem, size: M, quantity: 1}
  must_not_tools: []
  blocked: false                # lớp 1 có chặn không
  interrupt: true               # có sinh thẻ xác nhận không
  reply_language: vi            # vi | en
  rubric: "Xác nhận đã thêm đúng món sau khi có kết quả; không tự nêu giá mới"
split: dev                      # dev | test
```

Ca nhiều lượt liệt kê nhiều phần tử trong `turns`; `expect` áp cho cả hội thoại.

