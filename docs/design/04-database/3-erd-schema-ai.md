Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 3. ERD schema ai
## 3. ERD schema ai

11 bảng, do ai-service sở hữu. Cột ghi `ref core.*` là ID tham chiếu sang schema `core`, không có khóa ngoại. Bảng checkpoint của LangGraph nằm cùng schema nhưng do thư viện quản lý, dùng `conversations.id` làm mã luồng (thread).

```mermaid
erDiagram
  photo_consents {
    uuid id PK
    uuid user_id "ref core.users"
    varchar terms_version
    timestamptz accepted_at
  }
  user_photos {
    uuid id PK
    uuid user_id "ref core.users"
    varchar object_key
    char sha256
    timestamptz created_at
    timestamptz deleted_at
  }
  tryon_jobs {
    uuid id PK
    uuid user_id "ref core.users"
    varchar kind
    varchar status
    uuid photo_id FK
    uuid source_job_id FK
    uuid webcam_session_id FK
    varchar provider_ref
    varchar result_key
    varchar error
    timestamptz created_at
    timestamptz completed_at
    timestamptz media_deleted_at
  }
  tryon_job_items {
    uuid job_id PK, FK
    uuid variant_id PK "ref core.product_variants"
  }
  webcam_sessions {
    uuid id PK
    uuid user_id "ref core.users"
    jsonb target
    varchar provider_session_ref
    smallint max_seconds
    smallint used_seconds
    varchar status
    timestamptz started_at
    timestamptz ended_at
  }
  conversations {
    uuid id PK
    uuid user_id "ref core.users"
    varchar guest_session_id
    varchar actor_role
    timestamptz created_at
  }
  chat_messages {
    uuid id PK
    uuid conversation_id FK
    varchar role
    text content
    varchar trace_id
    varchar guardrail_flag
    jsonb cards
    timestamptz created_at
  }
  pending_actions {
    uuid id PK
    uuid conversation_id FK
    varchar tool_name
    jsonb args
    varchar status
    timestamptz expires_at
    timestamptz decided_at
    timestamptz created_at
  }
  outfit_suggestions {
    uuid id PK
    uuid conversation_id FK
    uuid anchor_variant_id "ref core.product_variants"
    jsonb sets
    timestamptz created_at
  }
  search_documents {
    varchar source_type PK
    uuid source_id PK "ref core.products or core.faqs"
    text content
    vector embedding
    bool visible
    timestamptz updated_at
  }
  ai_cost_records {
    uuid id PK
    varchar feature
    varchar provider
    int units
    numeric cost_usd
    uuid conversation_id FK
    uuid tryon_job_id FK
    uuid webcam_session_id FK
    timestamptz created_at
  }

  user_photos |o--o{ tryon_jobs : "input of"
  tryon_jobs |o--o| tryon_jobs : "video from"
  webcam_sessions |o--o{ tryon_jobs : snapshots
  tryon_jobs ||--o{ tryon_job_items : garments
  conversations ||--o{ chat_messages : contains
  conversations ||--o{ pending_actions : awaits
  conversations ||--o{ outfit_suggestions : suggests
  conversations |o--o{ ai_cost_records : costs
  tryon_jobs |o--o{ ai_cost_records : costs
  webcam_sessions |o--o{ ai_cost_records : costs
```

