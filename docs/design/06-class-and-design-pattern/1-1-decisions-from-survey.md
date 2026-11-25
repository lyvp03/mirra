Nguồn: 06-CLASS-AND-DESIGN-PATTERN.md > Mirra — B6: Thiết kế lớp và design pattern > 1. Quy ước và quyết định > 1.1 Quyết định từ khảo sát
### 1.1 Quyết định từ khảo sát

| Nội dung | Quyết định |
| --- | --- |
| Đơn vị vẽ | 9 sơ đồ lớp theo component ở B3 (core: Identity, Catalog, Ordering, Administration; ai: Assistant, TryOn, Webcam, Knowledge, Observability) + sequence mức thiết kế cho 4 luồng chính |
| Mức chi tiết | Thuộc tính có kiểu và chữ ký method cho service, domain, repository, adapter; model ORM chỉ ghi tên (cột xem B4); DTO tham chiếu B5 |
| Trạng thái đơn hàng | `OrderStateMachine` dùng bảng chuyển trạng thái |
| Design pattern | Trình bày đủ 6 pattern đã lên kế hoạch: Adapter/Strategy, State, Repository (+ Unit of Work), Factory, Observer, Template Method. State áp dụng ở dạng bảng chuyển trạng thái, là một cách cài đặt State mà sách GoF nêu trong phần Implementation (mục 6) |

