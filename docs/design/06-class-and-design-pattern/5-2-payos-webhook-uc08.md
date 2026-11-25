Nguồn: 06-CLASS-AND-DESIGN-PATTERN.md > Mirra — B6: Thiết kế lớp và design pattern > 5. Sequence mức thiết kế > 5.2 Webhook payOS (UC08)
### 5.2 Webhook payOS (UC08)

```mermaid
sequenceDiagram
  participant G as payOS
  participant R as PaymentsRouter
  participant PS as PaymentService
  participant GW as PayOSGateway
  participant U as UnitOfWork
  participant PY as PaymentRepository
  participant SM as OrderStateMachine
  participant N as Notifier
  G->>R: POST webhook (body)
  R->>PS: handle_payos_webhook(body)
  PS->>GW: parse_webhook(body)
  alt invalid signature
    GW-->>PS: AppError INVALID_SIGNATURE
    PS-->>R: 400
  else valid
    GW-->>PS: PaymentNotice(order_code, amount, reference)
    PS->>U: begin
    PS->>PY: get_by_txn(reference)
    alt already handled
      PS-->>R: 200
    else order already CANCELLED (paid after expiry)
      PS->>PY: mark PAID
      alt stock can be taken again
        PS->>SM: transition(order, AWAITING_CONFIRMATION, SYSTEM)
        SM-->>PS: side effects (take stock again)
      else out of stock
        PS->>PY: set REFUND_REQUIRED, order stays CANCELLED (BR09)
      end
      PS->>U: after_commit(notify payment channel, enqueue email)
      PS->>U: commit
      U->>N: notify("mirra:payment:{code}", new status)
      PS-->>R: 200
    else order AWAITING_PAYMENT
      PS->>PY: get_by_order(order) and check amount
      PS->>SM: transition(order, AWAITING_CONFIRMATION, SYSTEM)
      SM-->>PS: side effects (mark PAID)
      PS->>U: after_commit(notify payment channel, enqueue email)
      PS->>U: commit
      U->>N: notify("mirra:payment:{code}", PAID)
      PS-->>R: 200
    end
  end
```

