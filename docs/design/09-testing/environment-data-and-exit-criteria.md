Nguồn: 09-TESTING.md > B9 – Kế hoạch kiểm thử > Môi trường, dữ liệu và tiêu chí dừng
## Môi trường, dữ liệu và tiêu chí dừng

**Môi trường test.**

| Lớp | Môi trường | Ghi chú |
| --- | --- | --- |
| Unit / service | Local + CI, không hạ tầng ngoài | Mock adapter (FakeCore, FakePayos, FakeTryOn, FakeLLM) |
| Integration / contract | testcontainers: Postgres 17 + pgvector, Redis, MinIO | Dựng/xóa theo từng phiên test |
| E2E / load | Docker Compose staging giống VPS | Playwright + k6 chạy trên staging |

Staging dựng bằng chính bộ Docker Compose 10 container của sản phẩm, cấu hình giống VPS; các dịch vụ ngoài (PayOS, provider try-on thật) thay bằng adapter giả để test lặp lại được và không tốn phí; mỗi dịch vụ có driver thật riêng để chạy kiểm tra tích hợp định kỳ.

**Dữ liệu test.** Seed cố định (deterministic fixtures) cho: tài khoản mẫu (khách, admin), catalog từ ảnh thật (10 danh mục, 193 sản phẩm có biến thể màu/size, khoảng 15% SKU tồn ≤3 để thử biên, danh mục `jumpsuit` trống để thử trạng thái rỗng), đơn ở đủ 8 trạng thái, embedding mẫu cho pgvector. Dữ liệu nhạy cảm (ảnh thử đồ) dùng ảnh giả lập, không dùng dữ liệu người dùng thật.

**Tiêu chí dừng (exit criteria).**

| Tiêu chí | Ngưỡng |
| --- | --- |
| Độ phủ dòng domain + services | ≥ 70% |
| Ca test đặc tả ở mục 4 | đạt 100%, không lỗi nghiêm trọng |
| Lỗi mức cao (chặn luồng mua/thanh toán) | 0 tồn đọng |
| TTFT chat p95 | < 3 s trên staging |
| Eval AI agent (B7) | đạt ngưỡng đã định |
| Smoke test CI | xanh trước mỗi lần triển khai |

Độ phủ ≥ 70% áp cho tầng domain và services (nơi chứa logic nghiệp vụ); tầng adapter/UI ưu tiên ca then chốt hơn là con số phủ.
