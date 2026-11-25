Nguồn: 03-PACKAGE-COMPONENT-DEPLOYMENT.md > Mirra — B3: Package, Component, Deployment > 5. Sơ đồ deployment > 5.5 Môi trường dev
### 5.5 Môi trường dev

Cùng file Compose cộng một file override cho máy cá nhân:

- Mở cổng của từng container ra localhost (gồm console MinIO, giao diện Jaeger).
- Service Python chạy chế độ tự nạp lại khi sửa code, web chạy `next dev`; mã nguồn mount vào container.
- Caddy dùng chứng chỉ nội bộ cho `localhost`.
- Nhận webhook (payOS, try-on provider) qua một tunnel tạm trỏ về máy.

