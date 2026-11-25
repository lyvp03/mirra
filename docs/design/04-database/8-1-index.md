Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 8. Index, quy tắc xóa, dữ liệu seed > 8.1 Index
### 8.1 Index

PK và UNIQUE đã có index. PostgreSQL không tự tạo index cho khóa ngoại, nên chỉ thêm index phục vụ một truy vấn cụ thể dưới đây.

| Bảng | Index | Phục vụ |
| --- | --- | --- |
| auth\_tokens | (user\_id, kind) | Thu hồi refresh token khi khóa tài khoản (UC24, UC25) |
| addresses | (user\_id) | Sổ địa chỉ (UC04) |
| products | (category\_id, status) | Danh sách, lọc sản phẩm (UC05) |
| product\_images | (product\_id, position) | Trang sản phẩm |
| promotions | (product\_id, starts\_at) | Tìm khuyến mãi đang hiệu lực |
| orders | (user\_id, created\_at DESC) | Lịch sử đơn (UC09) |
| orders | (status, created\_at) | Lọc đơn (UC20.1), quét đơn quá hạn thanh toán (UC29) |
| order\_items | (variant\_id) | Sản phẩm bán chạy (UC26); kiểm tra khóa ngoại khi xóa biến thể |
| order\_status\_history | (order\_id, created\_at) | Dòng thời gian của đơn |
| inventory\_ledger | (variant\_id, created\_at) | Sổ kho theo biến thể (UC19.3) |
| setting\_history | (setting\_key, created\_at) | Lịch sử cấu hình |
| user\_photos | (user\_id) WHERE deleted\_at IS NULL | Ảnh đã lưu, giới hạn 3 ảnh |
| user\_photos | (created\_at) WHERE deleted\_at IS NULL | Job xóa ảnh 30 ngày (UC30) |
| tryon\_jobs | (user\_id, created\_at DESC) | Lịch sử thử đồ (UC14), đếm lượt trong ngày |
| tryon\_jobs | (photo\_id) | Xóa kết quả khi xóa ảnh (UC14.2), tra cache |
| webcam\_sessions | (user\_id, started\_at) | Giới hạn 1 phiên/ngày |
| webcam\_sessions | (started\_at) WHERE status = 'OPEN' | Tính ngân sách, dọn phiên bỏ dở |
| conversations | (user\_id, created\_at DESC) | Danh sách hội thoại, trace viewer (UC28) |
| chat\_messages | (conversation\_id, created\_at) | Hiển thị hội thoại, đếm hạn mức chat |
| pending\_actions | (conversation\_id) WHERE status = 'PENDING' | Tìm hành động đang chờ |
| search\_documents | HNSW (embedding vector\_cosine\_ops) | Tìm kiếm ngữ nghĩa cho agent, gợi ý phối đồ |
| ai\_cost\_records | (created\_at) | Tổng hợp chi phí theo kỳ (UC26) |

