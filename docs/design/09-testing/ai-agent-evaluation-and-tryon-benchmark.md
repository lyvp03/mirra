Nguồn: 09-TESTING.md > B9 – Kế hoạch kiểm thử > Đánh giá AI agent và benchmark try-on
## Đánh giá AI agent và benchmark try-on

**Đánh giá AI agent** là một nhánh test riêng, chi tiết ở [B7](https://claude.ai/artifact/JqesBMTsjrfCLztNEuy1sk) mục 7; B9 chỉ nhắc lại khung:

- Ma trận bao phủ: normal 40%, multi\_turn 15%, write 10%, attack 15%, out\_of\_scope 10%, missing\_info 10%; mỗi ô ≥ 3 ca.
- Chia dev 70% / test 30% (test đóng băng cho báo cáo). Chạy trên FakeCoreApiClient + fixture.
- Chấm: code (chọn tool, định dạng) + LLM chấm 1–5 theo rubric + người chấm lại 20%.
- Ngưỡng đạt: chọn tool ≥ 90%, vượt quyền 0, bịa giá 0, chặn nhầm ≤ 5%, chặn injection ≥ 90%, tuân thủ xác nhận 100%, chất lượng ≥ 4/5, TTFT p95 < 3 s.

**Benchmark nhà cung cấp try-on.** Nhà cung cấp try-on/video/realtime chưa chốt; benchmark này để chọn. Tiêu chí:

| Tiêu chí | Cách đo | Trọng số |
| --- | --- | --- |
| Chất lượng ghép đồ | 2 người chấm 1–5 (giống dáng, đúng màu/phom, ít lỗi) | Cao |
| Độ trễ mỗi ảnh | p50 / p95 (giây) | Cao |
| Chi phí mỗi ảnh / video | USD | Trung bình |
| Hỗ trợ webhook | Có webhook hay phải hỏi định kỳ | Trung bình |
| Ghép 2 món cho set | Ảnh ghép 1 trên + 1 dưới đúng cả 2 (BR20) | Cao |
| Nhận ảnh đồ trên người mẫu | Ảnh tham chiếu là ảnh người mẫu đang mặc (catalog không có flat-lay); lấy đúng món cần thử, kể cả từ ảnh set áo + quần/váy | Cao |
| Video 3–5 s | Có hỗ trợ, chất lượng | Thấp |
| Realtime webcam | Nhận ảnh tham chiếu, chặn phiên > 20 s từ server | Trung bình |
| Tự host được | Có thể chạy ngoài VPS, gọi qua HTTP | Thấp |

Quy trình: chuẩn bị bộ ảnh thử cố định (đa dạng dáng người và loại đồ) cùng bộ sản phẩm; chạy cùng bộ qua 2–3 nhà cung cấp; đo độ trễ và chi phí, 2 người chấm chất lượng theo rubric; tính điểm có trọng số rồi chọn. Bảng so sánh (điền sau benchmark):

| Tiêu chí | Nhà cung cấp A | Nhà cung cấp B | Nhà cung cấp C |
| --- | --- | --- | --- |
| Chất lượng (1–5) | \[đo sau\] | \[đo sau\] | \[đo sau\] |
| Độ trễ p95 (s) | \[đo sau\] | \[đo sau\] | \[đo sau\] |
| Chi phí / ảnh (USD) | \[đo sau\] | \[đo sau\] | \[đo sau\] |
| Webhook | \[đo sau\] | \[đo sau\] | \[đo sau\] |
| Ghép set | \[đo sau\] | \[đo sau\] | \[đo sau\] |
| Ảnh người mẫu | \[đo sau\] | \[đo sau\] | \[đo sau\] |
| **Điểm tổng** | \[đo sau\] | \[đo sau\] | \[đo sau\] |

