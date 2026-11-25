Nguồn: 05-API-CONTRACT-EVENTS.md > Mirra — B5: API, contract, sự kiện > 5. Contract các luồng chính > 5.3 Thử đồ bằng ảnh, set và video (UC12, UC13, UC14, UC32)
### 5.3 Thử đồ bằng ảnh, set và video (UC12, UC13, UC14, UC32)

1. Lần đầu: `GET /ai/v1/tryon/consent`, chưa đồng ý thì hiện hộp thoại rồi `POST /tryon/consent`.
2. Chọn ảnh đã lưu hoặc tải mới `POST /tryon/photos` (server kiểm ảnh người).
3. `POST /tryon/jobs` với `kind` = `IMAGE` (1 biến thể) hoặc `SET_IMAGE` (đúng 1 TOP + 1 BOTTOM).
4. Nhận 200 (kết quả có sẵn) hoặc 202 rồi mở `GET /tryon/jobs/{id}/stream` để nhận `job.completed` / `job.failed`.
5. Muốn có video: `POST /tryon/jobs/{id}/video`, theo dõi như bước 4.

```json
POST /ai/v1/tryon/jobs
Idempotency-Key: 0b5e...
{"kind": "SET_IMAGE", "photo_id": "p-01", "variant_ids": ["top-variant", "bottom-variant"]}

202
{"id": "j-01", "kind": "SET_IMAGE", "status": "PENDING", "items": [{"variant_id": "top-variant", "product_name": "Áo sơ mi lụa", "color": "Kem"}, {"variant_id": "bottom-variant", "product_name": "Chân váy xếp ly", "color": "Đen"}], "photo_id": "p-01", "created_at": "2026-11-03T09:00:00Z"}
```

| Lỗi | HTTP | Khi nào |
| --- | --- | --- |
| `EMAIL_NOT_VERIFIED` | 403 | BR19 |
| `CONSENT_REQUIRED` | 403 | Chưa đồng ý điều khoản hiện tại |
| `INVALID_PERSON_PHOTO` | 400 | Ảnh không đạt; `detail` nêu lý do để web hiện hướng dẫn chụp |
| `PHOTO_LIMIT_REACHED` | 409 | Đã có 3 ảnh |
| `TRYON_NOT_AVAILABLE` | 409 | Sản phẩm chưa bật thử đồ hoặc bị ẩn |
| `INVALID_SET` | 409 | Set không phải 1 TOP + 1 BOTTOM (BR20) |
| `SET_UNAVAILABLE` | 409 | Một món trong set hết hàng |
| `QUOTA_EXCEEDED` | 429 | Hết lượt ảnh hoặc video trong ngày; có `reset_at` |
| `FEATURE_DISABLED` | 503 | Admin tắt thử đồ |

Mã lỗi của job (`error_code` khi FAILED): `PROVIDER_ERROR`, `TIMEOUT` (quá 10 phút), `INVALID_RESULT`. Job FAILED không trừ lượt.

