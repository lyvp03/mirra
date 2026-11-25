Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 1. Quy ước và quyết định
## 1. Quy ước và quyết định

B4 chuyển entity của B2 thành bảng PostgreSQL 17 theo chuẩn 3NF, chia hai schema theo ranh giới service ở B3. Nguyên tắc: mỗi cột phải phục vụ ít nhất một UC hoặc một quy tắc nghiệp vụ; giá trị tính được từ dữ liệu khác thì không lưu, trừ các ngoại lệ có lý do ở mục 6.

