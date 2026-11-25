Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 7. Kế hoạch đánh giá agent > 7.1 Quyết định đã chốt (08/11)
### 7.1 Quyết định đã chốt (08/11)

| Vấn đề | Chốt |
| --- | --- |
| Bộ test | B7 đưa ra cấu trúc ca test, ma trận bao phủ và quy tắc sinh; Ly dùng model khác để sinh ca theo các quy tắc này |
| Cách chấm | Kiểm bằng code + LLM chấm chất lượng theo rubric + người chấm lại 20% |
| Môi trường | Core giả với dữ liệu cố định, cộng khoảng 10 ca end-to-end trên môi trường thật đã seed |
| Ngưỡng đạt | Chọn đúng tool ≥ 90%; vượt quyền = 0; bịa giá = 0; chặn nhầm ≤ 5% (chi tiết mục 7.7) |

Thử đồ (so sánh 2–3 provider) không nằm trong mục này, vì đó là đánh giá provider chứ không phải agent; phần đó thuộc kế hoạch benchmark và B9.

