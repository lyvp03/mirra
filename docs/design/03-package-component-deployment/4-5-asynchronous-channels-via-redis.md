Nguồn: 03-PACKAGE-COMPONENT-DEPLOYMENT.md > Mirra — B3: Package, Component, Deployment > 4. Sơ đồ component > 4.5 Kênh bất đồng bộ qua Redis
### 4.5 Kênh bất đồng bộ qua Redis

| Kênh | Kiểu | Bên ghi | Bên đọc | Dùng cho |
| --- | --- | --- | --- | --- |
| IEventStream: sự kiện sản phẩm, FAQ | Redis Streams, consumer group | core\_api (sau commit) | ai\_worker (`IndexSyncConsumer`) | Cập nhật SearchDocument và embedding |
| IEventStream: sự kiện cấu hình | Redis Streams | core\_api | ai\_service, ai\_worker | Làm mới cấu hình đệm (hạn mức chat, lượt thử, webcam) |
| IJobQueue: email | Redis Streams, consumer group | core\_api | core\_worker (`EmailConsumer`) | Gửi email xác thực, đặt lại mật khẩu, trạng thái đơn |
| IJobQueue: try-on | Redis Streams, consumer group | ai\_service | ai\_worker (`TryOnJobRunner`) | Gọi provider, lưu kết quả, hoàn lượt khi lỗi hoặc quá 10 phút |
| Tiến trình job, trạng thái thanh toán | Redis pub/sub | ai\_worker, core\_api | ai\_service, core\_api | Đẩy SSE tới trình duyệt |

Tên stream, định dạng thông điệp và cách thử lại để B5.

