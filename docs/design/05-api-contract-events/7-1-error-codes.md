Nguồn: 05-API-CONTRACT-EVENTS.md > Mirra — B5: API, contract, sự kiện > 7. Mã lỗi và khóa cấu hình > 7.1 Mã lỗi (`code`)
### 7.1 Mã lỗi (`code`)

| Nhóm | Code | HTTP |
| --- | --- | --- |
| Chung | `VALIDATION_ERROR` | 422 |
|  | `UNAUTHENTICATED`, `FORBIDDEN`, `NOT_FOUND` | 401, 403, 404 |
|  | `RATE_LIMITED` | 429 |
|  | `FEATURE_DISABLED` | 503 |
|  | `FILE_TOO_LARGE`, `UNSUPPORTED_FILE_TYPE` | 413, 415 |
| Tài khoản | `EMAIL_TAKEN` | 409 |
|  | `WEAK_PASSWORD` | 422 |
|  | `INVALID_CREDENTIALS` | 401 |
|  | `LOGIN_TEMPORARILY_LOCKED` | 429 |
|  | `ACCOUNT_LOCKED` | 403 |
|  | `TOKEN_INVALID_OR_EXPIRED` (link xác thực, đặt lại, mời) | 400 |
|  | `EMAIL_NOT_VERIFIED` | 403 |
|  | `ADDRESS_LIMIT_REACHED` | 409 |
| Sản phẩm (quản trị) | `SLUG_TAKEN`, `SKU_TAKEN` | 409 |
|  | `FLAT_LAY_REQUIRED` (thiếu ảnh tham chiếu thử đồ, hoặc sản phẩm phụ kiện; giữ tên cũ) | 409 |
|  | `NOT_PUBLISHABLE` (thiếu giá, ảnh hoặc biến thể) | 409 |
|  | `PRODUCT_HAS_ORDERS` | 409 |
|  | `PROMOTION_OVERLAP` | 409 |
|  | `INVALID_QUANTITY` (tồn âm) | 409 |
|  | `DRAFT_FAILED` (UC18) | 502 |
| Đơn hàng | `PRICE_CHANGED`, `OUT_OF_STOCK`, `PRODUCT_UNAVAILABLE` | 409 |
|  | `INVALID_WARD` | 422 |
|  | `CANNOT_CANCEL`, `INVALID_TRANSITION` | 409 |
|  | `PHONE_CHECK_REQUIRED` (BR13) | 409 |
|  | `ORDER_TOKEN_EXPIRED` (BR12) | 410 |
|  | `REVIEW_NOT_ALLOWED`, `ALREADY_REVIEWED` | 409 |
|  | `PAYMENT_GATEWAY_ERROR` | 502 |
|  | `INVALID_SIGNATURE` (webhook) | 400 |
| Trợ lý | `CHAT_LIMIT_REACHED` | 429 |
|  | `GUEST_SESSION_INVALID` | 401 |
|  | `CONVERSATION_CLOSED` (hội thoại đã quá số ngày không hoạt động) | 409 |
|  | `ACTION_EXPIRED`, `ACTION_ALREADY_DECIDED` | 409 |
|  | `LLM_UNAVAILABLE`, `GUARDRAIL_BLOCKED`, `AGENT_STEP_LIMIT` | qua sự kiện SSE `error` |
| Thử đồ | `CONSENT_REQUIRED` | 403 |
|  | `INVALID_PERSON_PHOTO` | 400 |
|  | `PHOTO_LIMIT_REACHED`, `TRYON_NOT_AVAILABLE`, `INVALID_SET`, `SET_UNAVAILABLE` | 409 |
|  | `QUOTA_EXCEEDED` | 429 |
|  | `AI_BUDGET_EXCEEDED` (NFR13; cả video, webcam, sinh nháp sản phẩm) | 503 |
|  | Job: `PROVIDER_ERROR`, `TIMEOUT`, `INVALID_RESULT` | trong `error_code` của job |
| Webcam | `WEBCAM_DAILY_LIMIT` | 429 |
|  | `WEBCAM_BUDGET_EXHAUSTED` | 503 |
|  | `SESSION_NOT_OPEN` | 409 |
|  | `REALTIME_PROVIDER_ERROR` | 502 |
| Cấu hình | `UNKNOWN_SETTING` | 404 |
|  | `INVALID_SETTING_VALUE` | 422 |

