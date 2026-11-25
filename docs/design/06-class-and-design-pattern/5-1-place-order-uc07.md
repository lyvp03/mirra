Nguồn: 06-CLASS-AND-DESIGN-PATTERN.md > Mirra — B6: Thiết kế lớp và design pattern > 5. Sequence mức thiết kế > 5.1 Đặt hàng (UC07)
### 5.1 Đặt hàng (UC07)

```mermaid
sequenceDiagram
  participant R as OrdersRouter
  participant I as IdempotencyStore
  participant S as OrderService
  participant U as UnitOfWork
  participant VR as VariantRepository
  participant PR as PricingService
  participant SF as ShippingFeeStrategy
  participant SP as StockPolicy
  participant OR as OrderRepository
  participant PS as PaymentService
  participant GW as PayOSGateway
  R->>I: get(idem_key, "orders")
  alt key seen
    I-->>R: saved response
  else new
    R->>S: place(cmd, buyer, idem_key)
    S->>U: begin
    S->>VR: lock_many(variant_ids)
    S->>PR: effective_prices(variant_ids, now)
    S->>SF: quote(ward, weight_g, subtotal)
    S->>S: compare total with cmd.expected_total
    alt total differs
      S-->>R: AppError PRICE_CHANGED
    else
      S->>SP: take(variants, lines)
      alt not enough stock
        SP-->>S: AppError OUT_OF_STOCK
      else
        S->>OR: add(order, items, history)
        S->>U: add ledger drafts
        S->>PS: start(order)
        PS->>PS: create Payment UNPAID
        S->>U: after_commit(enqueue ORDER_PLACED email)
        S->>U: commit
        opt VIETQR
          PS->>GW: create_link(code, amount, desc, expires_at)
          GW-->>PS: PaymentLink
          PS->>U: save gateway_ref (own transaction)
        end
        S-->>R: PlacedOrder
        R->>I: save(idem_key, response, 24h)
      end
    end
  end
```

Gọi payOS sau commit để không giữ khóa dòng biến thể trong lúc chờ mạng; nếu payOS lỗi, đơn vẫn tồn tại ở AWAITING\_PAYMENT và trang thanh toán gọi lại `PaymentService.get` để tạo link (B5 mục 5.1, `PAYMENT_GATEWAY_ERROR`).

