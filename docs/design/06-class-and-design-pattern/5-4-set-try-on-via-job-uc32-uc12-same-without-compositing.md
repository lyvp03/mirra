Nguồn: 06-CLASS-AND-DESIGN-PATTERN.md > Mirra — B6: Thiết kế lớp và design pattern > 5. Sequence mức thiết kế > 5.4 Thử set qua job (UC32; UC12 giống nhưng không ghép ảnh)
### 5.4 Thử set qua job (UC32; UC12 giống nhưng không ghép ảnh)

```mermaid
sequenceDiagram
  participant R as TryOnRouter
  participant S as TryOnService
  participant K as CoreApiClient
  participant SR as SetRule
  participant JR as TryOnJobRepository
  participant Q as TryOnQuotaPolicy
  participant U as UnitOfWork
  participant JQ as JobQueue
  participant W as TryOnJobConsumer
  participant RN as SetImageJobRunner
  participant OC as OutfitComposer
  participant P as TryOnProvider
  participant N as Notifier
  R->>S: create_job(user, cmd, idem_key)
  S->>S: check email_verified and consent
  S->>K: internal("/variants", ids)
  S->>SR: validate(items)
  S->>JR: find_cached(photo_sha256, variant_ids)
  alt cached
    S-->>R: 200 COMPLETED job
  else
    S->>JR: count_completed_today(user, kinds)
    S->>Q: ensure_available(used, kind, limits)
    S->>U: add job PENDING + items
    S->>U: after_commit(enqueue tryon.run)
    S->>U: commit
    U->>JQ: enqueue("mirra:jobs:tryon", job_id)
    S-->>R: 202 PENDING job
  end
  JQ-->>W: tryon.run(job_id)
  W->>RN: run(job_id)
  RN->>RN: load_inputs(job)
  RN->>OC: compose(top, bottom)
  RN->>P: submit_image(person, composite, callback_url)
  P-->>RN: provider_ref
  RN->>JR: set PROCESSING, provider_ref
  RN->>N: notify job PROCESSING
  P->>R: POST /webhooks/tryon
  R->>S: handle_callback(body, headers)
  S->>P: parse_callback(body, headers)
  S->>JR: get_by_provider_ref(ref)
  S->>S: store result in bucket tryon, set COMPLETED, record cost
  S->>N: notify job COMPLETED
```

