Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 1. Quy ước và quyết định > 1.1 Quyết định từ khảo sát
### 1.1 Quyết định từ khảo sát

| Nội dung | Quyết định |
| --- | --- |
| Khóa chính | `uuid`, sinh bằng `gen_random_uuid()` hoặc ở ứng dụng; đơn hàng có thêm mã ngắn `code` cho người dùng |
| JSONB | Chỉ cho dữ liệu lưu và đọc nguyên khối, không lọc hay nối theo phần tử bên trong; mỗi cột JSONB ghi lý do ở mục 6 |
| Lịch sử chat | Bảng `chat_messages` riêng; bảng checkpoint của LangGraph do thư viện tạo và quản lý, không vẽ vào ERD |
| Ngôn ngữ nội dung | Tiếng Việt; riêng tên sản phẩm là tên thương mại tiếng Anh (`name`) kèm tên mô tả tiếng Việt (`name_vi`) cho tìm kiếm; song ngữ chỉ ở giao diện |

