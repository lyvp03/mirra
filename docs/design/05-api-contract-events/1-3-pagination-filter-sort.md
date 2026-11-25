Nguồn: 05-API-CONTRACT-EVENTS.md > Mirra — B5: API, contract, sự kiện > 1. Quy ước chung > 1.3 Phân trang, lọc, sắp xếp
### 1.3 Phân trang, lọc, sắp xếp

- Danh sách dùng `?page=1&page_size=20` (`page_size` tối đa 100). Phản hồi: `{"items": [...], "page": 1, "page_size": 20, "total": 135}`.
- Lọc bằng tham số query cùng tên cột (`status=CONFIRMED`, `category=ao-so-mi`).
- Sắp xếp `sort=field` hoặc `sort=-field` (giảm dần), chỉ trên các trường mỗi endpoint liệt kê.

