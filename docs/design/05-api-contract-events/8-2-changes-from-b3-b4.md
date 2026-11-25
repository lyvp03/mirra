Nguồn: 05-API-CONTRACT-EVENTS.md > Mirra — B5: API, contract, sự kiện > 8. File OpenAPI và điểm cần kiểm chứng > 8.2 Thay đổi so với B3, B4
### 8.2 Thay đổi so với B3, B4

| Chỗ | Thay đổi | Lý do |
| --- | --- | --- |
| `orders.code` (B4) | Cố định 10 chữ số | payOS yêu cầu `orderCode` là số nguyên; dùng chung một mã |
| ICoreInternal (B3) | Bỏ endpoint trạng thái tài khoản; thêm `/variants` và `/index-documents` | Vai trò và xác thực email đã có trong JWT; sự kiện chỉ mang ID |
| Khóa `settings` (B4) | Chốt danh sách ở mục 7.2 | B4 để lại cho B5 |

