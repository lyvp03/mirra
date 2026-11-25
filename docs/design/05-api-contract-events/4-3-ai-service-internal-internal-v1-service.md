Nguồn: 05-API-CONTRACT-EVENTS.md > Mirra — B5: API, contract, sự kiện > 4. Endpoint ai-service và endpoint nội bộ > 4.3 ai-service nội bộ (`/internal/v1`, Service)
### 4.3 ai-service nội bộ (`/internal/v1`, Service)

| Method | Path | Người gọi | Dùng cho |
| --- | --- | --- | --- |
| GET | `/usage/summary?from&to` | core-api (`ReportService`) | Số job thử đồ theo loại và tỉ lệ thành công, số giây webcam, số hội thoại theo vai trò, chi phí theo tính năng, chi phí theo ngày (`by_day`), trạng thái trần tháng (`budget`: đã dùng, trần, tỉ lệ, cờ cảnh báo từ 80%) (UC26, NFR13) |

