Nguồn: 04-DATABASE.md > Mirra — B4: Thiết kế cơ sở dữ liệu > 4. Từ điển dữ liệu schema core
## 4. Từ điển dữ liệu schema core

Cột `id uuid PK` và `created_at timestamptz NOT NULL DEFAULT now()` không nhắc lại ở từng bảng. Mặc định mọi cột `NOT NULL`; cột cho phép rỗng ghi `NULL`.

