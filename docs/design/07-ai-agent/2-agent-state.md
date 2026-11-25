Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 2. State của agent
## 2. State của agent

State là dữ liệu graph mang theo qua từng bước. Sau mỗi bước, checkpoint ghi state xuống Postgres (schema `ai`), nhờ vậy graph dừng ở `interrupt` rồi chạy tiếp được ở một request khác. Vì bị ghi xuống DB, state chỉ nên chứa những gì cần để chạy tiếp hội thoại: không chứa bí mật, không chứa thứ tính lại được.

