Nguồn: 05-API-CONTRACT-EVENTS.md > Mirra — B5: API, contract, sự kiện > 4. Endpoint ai-service và endpoint nội bộ > 4.1 ai-service công khai (`/ai/v1`)
### 4.1 ai-service công khai (`/ai/v1`)

| Method | Path | Quyền | UC | Chi tiết | Ghi chú |
| --- | --- | --- | --- | --- | --- |
| POST | `/chat/guest-sessions` | Public | UC15 |  | Cấp `guest_session_id` |
| GET, POST | `/chat/conversations` | Any | UC15, UC31 |  | Tạo kèm `context.product_slug` khi mở từ trang sản phẩm |
| GET | `/chat/conversations/{id}/messages` | Any (chủ hội thoại) | UC15 |  | Mỗi tin kèm `cards` (danh sách thẻ, B7 mục 4.3) để mở lại vẫn thấy thẻ; hội thoại đã đóng vẫn xem được |
| POST | `/chat/conversations/{id}/messages` | Any | UC15 | ✓ | Trả SSE. Còn thao tác chờ xác nhận thì tự chuyển EXPIRED và phát `action.result` trước (B7 mục 2.6). Không có tin mới quá `chat.conversation_idle_days` ngày thì 409 `CONVERSATION_CLOSED` |
| POST | `/chat/actions/{id}/confirm` | Any (chủ hội thoại) | UC16 | ✓ | Trả SSE, agent chạy tiếp |
| POST | `/chat/actions/{id}/reject` | Any (chủ hội thoại) | UC16 | ✓ | Trả SSE |
| GET | `/outfits/{id}` | Any (chủ hội thoại) | UC31, UC32 |  | Vẽ lại thẻ set, giá và tồn lấy mới từ core |
| GET | `/tryon/consent` | Verified | UC12.1 |  | Phiên bản điều khoản hiện tại, đã đồng ý chưa |
| POST | `/tryon/consent` | Verified | UC12.1 |  | `{terms_version}` |
| GET | `/tryon/quota` | Verified | UC12.3 |  | Lượt ảnh, video còn lại hôm nay |
| GET, POST | `/tryon/photos` | Verified | UC14.2, UC12.2 | ✓ | POST multipart; kiểm ảnh người; tối đa 3 ảnh |
| DELETE | `/tryon/photos/{id}` | Verified | UC14.2 |  | Xóa cả kết quả từ ảnh này |
| POST | `/tryon/jobs` | Verified | UC12, UC32 | ✓ | `Idempotency-Key`; 202 hoặc 200 nếu có sẵn kết quả |
| POST | `/tryon/jobs/{id}/video` | Verified | UC13 | ✓ | `Idempotency-Key`; 202 |
| GET | `/tryon/jobs/{id}` | Verified (chủ job) | UC12, UC13 | ✓ |  |
| GET | `/tryon/jobs/{id}/stream` | Verified (chủ job) | UC12, UC13 | ✓ | SSE tiến trình |
| GET | `/tryon/history` | Verified | UC14.1 |  | Job COMPLETED, kèm URL ký |
| GET | `/webcam/availability` | Verified | UC33 | ✓ | Còn phiên hôm nay và còn ngân sách không, để hiện/ẩn nút |
| POST | `/webcam/sessions` | Verified | UC33 | ✓ | Trả token ngắn hạn của provider |
| POST | `/webcam/sessions/{id}/end` | Verified (chủ phiên) | UC33 | ✓ | `{used_seconds}` |
| POST | `/webcam/sessions/{id}/snapshots` | Verified (chủ phiên) | UC33 | ✓ | multipart khung hình → job WEBCAM\_SNAPSHOT |
| POST | `/product-drafts` | Staff | UC18 |  | multipart 1–4 ảnh + `note`; trả bản nháp, không lưu |
| GET | `/admin/conversations` | Admin | UC28 |  | `user_id, from, to, flagged` |
| GET | `/admin/conversations/{id}` | Admin | UC28 |  | Tin nhắn, hành động chờ, span từ Langfuse (nếu lấy được) |
| POST | `/webhooks/tryon` | Try-on provider | UC12, UC13 | ✓ |  |

