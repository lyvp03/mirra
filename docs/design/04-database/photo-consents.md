Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 5. Từ điển dữ liệu schema ai > 5.1 photo\_consents — đồng ý dùng ảnh (UC12.1, Luật 91/2025/QH15)
### 5.1 photo\_consents — đồng ý dùng ảnh (UC12.1, Luật 91/2025/QH15)

| Cột | Kiểu | Ràng buộc | Ý nghĩa |
| --- | --- | --- | --- |
| user\_id | uuid | ref users; UNIQUE (user\_id, terms\_version) |  |
| terms\_version | varchar(20) |  | Phiên bản điều khoản đã đồng ý |
| accepted\_at | timestamptz | DEFAULT now() |  |

Không có `created_at` (trùng `accepted_at`).

