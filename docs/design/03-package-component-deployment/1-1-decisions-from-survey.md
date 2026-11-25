Nguồn: 03-PACKAGE-COMPONENT-DEPLOYMENT.md > Mirra — B3: Package, Component, Deployment > 1. Quy ước và quyết định > 1.1 Quyết định từ khảo sát
### 1.1 Quyết định từ khảo sát

| Nội dung | Quyết định |
| --- | --- |
| Chia package | Theo service (web, core-api, ai-service, worker), bên trong mỗi service chia theo tầng |
| Kiến trúc trong service Python | Phân tầng: api → service → repository → model; mọi hệ thống ngoài đi qua interface + adapter |
| Ký hiệu | Mermaid xấp xỉ UML (subgraph = package/node, mũi tên = phụ thuộc hoặc kết nối); vẽ lại chuẩn UML trong Astah |
| Category, SizeChart | Nạp sẵn bằng seed khi triển khai, không có màn hình quản lý; AdminUnit cũng nạp sẵn từ danh mục hành chính |
| Môi trường | Dev chạy Docker Compose trên máy cá nhân; production là 1 VPS chạy cùng bộ Compose |

