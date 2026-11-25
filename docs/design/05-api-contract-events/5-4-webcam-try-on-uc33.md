Nguồn: 05-API-CONTRACT-EVENTS.md > Mirra — B5: API, contract, sự kiện > 5. Contract các luồng chính > 5.4 Thử đồ qua webcam (UC33)
### 5.4 Thử đồ qua webcam (UC33)

1. Trang sản phẩm và thẻ trong chat gọi `GET /ai/v1/webcam/availability` để hiện hoặc ẩn nút.
2. Bấm nút: `POST /webcam/sessions` với 1 hoặc 2 `variant_ids`. Server giữ chỗ 20 giây trong ngân sách, tạo phiên phía provider và trả `provider_session`.
3. Web xin quyền camera; bị từ chối thì gọi `/end` với `used_seconds = 0` và chuyển sang thử bằng ảnh.
4. Web nối WebRTC thẳng tới provider bằng `provider_session`, đếm ngược 20 giây; chụp khung hình bằng `POST /webcam/sessions/{id}/snapshots`.
5. Kết thúc: `POST /webcam/sessions/{id}/end`. Server tự dừng phiên phía provider khi hết 20 giây; phiên bỏ dở do job dọn đóng và tính đủ 20 giây.

| Lỗi | HTTP | Khi nào |
| --- | --- | --- |
| `EMAIL_NOT_VERIFIED`, `CONSENT_REQUIRED` | 403 | Như 5.3 |
| `WEBCAM_DAILY_LIMIT` | 429 | Đã dùng 1 phiên hôm nay |
| `WEBCAM_BUDGET_EXHAUSTED` | 503 | Hết ngân sách toàn hệ thống |
| `INVALID_SET`, `TRYON_NOT_AVAILABLE` | 409 | Như 5.3 |
| `SESSION_NOT_OPEN` | 409 | Gửi khung hình hoặc đóng phiên đã đóng |
| `REALTIME_PROVIDER_ERROR` | 502 | Không tạo được phiên phía provider; ngân sách đã giữ được trả lại |

`used_seconds` do web báo; server chặn trong khoảng 0 đến `max_seconds` và ưu tiên thời lượng provider báo về nếu adapter lấy được.

