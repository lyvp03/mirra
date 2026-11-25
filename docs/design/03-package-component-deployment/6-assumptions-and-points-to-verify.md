Nguồn: 03-PACKAGE-COMPONENT-DEPLOYMENT.md > Mirra — B3: Package, Component, Deployment > 6. Giả định và điểm cần kiểm chứng
## 6. Giả định và điểm cần kiểm chứng

| Giả định | Ảnh hưởng nếu sai | Kiểm chứng |
| --- | --- | --- |
| Try-on provider trả kết quả qua webhook (`ITryOnCallback`) | Nếu chỉ hỗ trợ hỏi kết quả, `TryOnJobRunner` ở ai\_worker chuyển sang hỏi định kỳ; interface `TryOnProvider` không đổi | Benchmark 31/10 – 06/11 |
| Nếu tự host mô hình try-on, mô hình chạy ngoài VPS và được gọi qua HTTP như một provider | Nếu phải chạy trên VPS thì cần thêm container và VPS có GPU | Benchmark |
| Dịch vụ realtime cho trình duyệt nối WebRTC trực tiếp bằng token ngắn hạn do server cấp, và server dừng được phiên | Nếu phải chuyển luồng qua server thì ai\_service cần thêm thành phần relay media | Benchmark |
| Cấu hình VPS đủ cho 10 container | Phải nâng VPS hoặc bỏ Jaeger khỏi production | Chạy thử bộ Compose đầy đủ trước khi chọn gói VPS |
| Trace của Jaeger lưu trong bộ nhớ là đủ | Mất trace khi container khởi động lại; trace của agent vẫn còn ở Langfuse | Chấp nhận cho phạm vi đồ án |
