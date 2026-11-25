Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 2. ERD schema core
## 2. ERD schema core

21 bảng, do core-api sở hữu. Để sơ đồ đọc được, ba quan hệ "người thực hiện" không vẽ: `order_status_history.actor_id`, `inventory_ledger.actor_id`, `setting_history.actor_id` đều tham chiếu `users.id` (xem mục 4).

```mermaid
erDiagram
  users {
    uuid id PK
    varchar email UK
    varchar password_hash
    varchar full_name
    varchar phone
    varchar role
    varchar status
    varchar locked_reason
    timestamptz email_verified_at
    timestamptz created_at
  }
  auth_tokens {
    uuid id PK
    uuid user_id FK
    varchar kind
    char token_hash UK
    timestamptz expires_at
    timestamptz used_at
  }
  provinces {
    varchar code PK
    varchar name
  }
  wards {
    varchar code PK
    varchar province_code FK
    varchar name
    float lat
    float lng
  }
  addresses {
    uuid id PK
    uuid user_id FK
    varchar receiver_name
    varchar phone
    varchar ward_code FK
    varchar street
    bool is_default
  }
  categories {
    uuid id PK
    varchar name
    varchar slug UK
    varchar slot
  }
  size_charts {
    uuid id PK
    varchar name
    jsonb measurements
  }
  products {
    uuid id PK
    uuid category_id FK
    uuid size_chart_id FK
    varchar name
    varchar name_vi
    varchar slug UK
    text description
    varchar material
    int price
    varchar status
    bool try_on_enabled
    bool ai_generated
    timestamptz created_at
    timestamptz updated_at
  }
  product_variants {
    uuid id PK
    uuid product_id FK
    varchar sku UK
    varchar color
    varchar color_hex
    varchar size
    int weight_gram
    int stock
  }
  product_images {
    uuid id PK
    uuid product_id FK
    varchar color
    varchar kind
    varchar object_key
    smallint position
  }
  promotions {
    uuid id PK
    uuid product_id FK
    int sale_price
    timestamptz starts_at
    timestamptz ends_at
  }
  cart_items {
    uuid user_id PK, FK
    uuid variant_id PK, FK
    smallint quantity
  }
  orders {
    uuid id PK
    varchar code UK
    uuid user_id FK
    varchar guest_email
    char guest_token_hash
    varchar receiver_name
    varchar receiver_phone
    varchar ward_code FK
    varchar street
    int shipping_fee
    varchar status
    varchar tracking_no
    timestamptz created_at
    timestamptz updated_at
  }
  order_items {
    uuid order_id PK, FK
    uuid variant_id PK, FK
    varchar product_name
    varchar color
    varchar size
    int unit_price
    smallint quantity
  }
  order_status_history {
    uuid id PK
    uuid order_id FK
    varchar status
    uuid actor_id FK
    varchar note
    timestamptz created_at
  }
  payments {
    uuid id PK
    uuid order_id FK, UK
    varchar method
    varchar status
    int amount
    varchar gateway_ref
    varchar txn_id UK
    timestamptz paid_at
    varchar refund_txn_ref
    timestamptz refunded_at
  }
  inventory_ledger {
    uuid id PK
    uuid variant_id FK
    int delta
    varchar reason
    uuid order_id FK
    uuid actor_id FK
    varchar note
    timestamptz created_at
  }
  reviews {
    uuid order_id PK, FK
    uuid variant_id PK, FK
    smallint rating
    text content
    bool hidden
    timestamptz created_at
  }
  faqs {
    uuid id PK
    varchar question
    text answer
    varchar kind
    bool active
    timestamptz updated_at
  }
  settings {
    varchar key PK
    jsonb value
  }
  setting_history {
    uuid id PK
    varchar setting_key FK
    jsonb new_value
    uuid actor_id FK
    timestamptz created_at
  }

  users ||--o{ auth_tokens : has
  users ||--o{ addresses : has
  provinces ||--|{ wards : contains
  wards ||--o{ addresses : locates
  wards ||--o{ orders : "ships to"
  categories ||--o{ products : groups
  size_charts |o--o{ products : sizes
  products ||--|{ product_variants : has
  products ||--o{ product_images : has
  products ||--o{ promotions : has
  users ||--o{ cart_items : owns
  product_variants ||--o{ cart_items : "in cart"
  users |o--o{ orders : places
  orders ||--|{ order_items : contains
  product_variants ||--o{ order_items : "sold as"
  orders ||--|{ order_status_history : logs
  orders ||--|| payments : "paid by"
  product_variants ||--o{ inventory_ledger : moves
  orders |o--o{ inventory_ledger : causes
  order_items ||--o| reviews : reviewed
  settings ||--|{ setting_history : logs
```

