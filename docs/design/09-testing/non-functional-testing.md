Nguồn: 09-TESTING.md > B9 – Kế hoạch kiểm thử > Kiểm thử phi chức năng
## Kiểm thử phi chức năng

**Load test (k6).** Chạy trên môi trường staging cấu hình giống VPS; dùng Fake cho try-on để không tốn phí (chỉ đo độ trễ provider thật một lần riêng ở benchmark mục 6).

| Kịch bản | Tải mục tiêu | Chỉ số quan tâm |
| --- | --- | --- |
| Duyệt danh sách + chi tiết SP (đọc) | ramp tới \~50 VU đồng thời | p95 latency, throughput |
| Thêm giỏ + checkout (ghi) | \~15 VU | p95, error rate, không cạn pool DB |
| Chat SSE | \~10 VU | TTFT p95, số stream đồng thời |
| Try-on job (bất đồng bộ) | \~10 job/phút | tồn đọng hàng đợi, thời gian hoàn thành |

Tiêu chí chung: error rate < 1%, pool kết nối DB không cạn, p95 trong ngưỡng NFR. Con số VU ở trên là mức khởi điểm hợp với quy mô đồ án trên 1 VPS, điều chỉnh theo ngưỡng thực trong tài liệu Nguồn.

**Đối chiếu NFR01–13.**

| Nhóm | Yêu cầu | Cách kiểm |
| --- | --- | --- |
| Hiệu năng API | Thời gian phản hồi đọc/ghi dưới ngưỡng | k6 load test, đo p95 mỗi endpoint |
| Hiệu năng chat | TTFT p95 < 3 s | Bộ eval agent + k6 kịch bản chat |
| Khả dụng / tin cậy | Webhook idempotent; sao lưu 02:00 giữ 7 bản; job khôi phục được | Integration test idempotent; thử phục hồi từ bản pg\_dump |
| Bảo mật | JWT RS256, access trong bộ nhớ, refresh httpOnly xoay vòng; khóa 5 lần/15'; phân quyền tool; chặn injection | Unit/integration auth; ca G4 và nhóm H ở mục 4; rà soát thủ công |
| Dữ liệu cá nhân | Ảnh thử đồ xóa sau 30 ngày; cần đồng ý; xóa tài khoản thủ công | Kiểm job xóa ảnh; ca F5; quy trình xóa |
| Chi phí AI | Trần $100/tháng, 80% cảnh báo, chạm trần tắt tính năng AI | Unit CostGuard; luật R4 bảng quyết định mục 3 |
| Giao diện | UI song ngữ, nội dung tiếng Việt; responsive desktop + mobile | Checklist thủ công theo B8 |

Nội dung từng NFR01–13 lấy theo tài liệu Nguồn; bảng trên gom theo nhóm và gắn cách kiểm tương ứng.

