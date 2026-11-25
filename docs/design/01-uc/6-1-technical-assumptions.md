Nguồn: 01-UC.md > Mirra — B1: Phân rã và đặc tả use case > 6. Giả định cần kiểm chứng và giá trị đã chốt > 6.1 Giả định kỹ thuật
### 6.1 Giả định kỹ thuật

- [ ] **Thử set bằng ảnh ghép:** dịch vụ thử đồ nhận một ảnh ghép 2 món và mặc đúng cả 2 món trong một lần chạy. Benchmark so với cách chạy 2 bước nối tiếp trên cùng bộ ảnh. Nếu không đạt, cần chốt lại cách thử set và cách tính lượt.
- [ ] **Gợi ý phối đồ đủ tốt:** `suggest_outfit` cần sản phẩm có loại món (trên/dưới/liền/phụ kiện), màu và tag dịp mặc. Kiểm tra bằng 20 yêu cầu phối đồ mẫu trên bộ dữ liệu thật.

* [ ] **Webcam realtime:** dịch vụ realtime nhận được ảnh tham chiếu là ảnh ghép 2 món và giữ được trang phục ổn định khi khách cử động; token ngắn hạn hoặc API của nhà cung cấp cho phép chặn phiên quá 20 giây từ phía server. Nếu không chặn được từ server, giới hạn chỉ dựa vào trình duyệt và cần giữ trần ngân sách thấp.

