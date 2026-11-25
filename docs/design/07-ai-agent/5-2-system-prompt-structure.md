Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 5. Prompt > 5.2 Cấu trúc system prompt
### 5.2 Cấu trúc system prompt

`PromptBuilder` ghép system prompt ở mỗi lượt theo thứ tự cố định. Phần không đổi đặt trước, phần thay đổi đặt cuối:

| Thứ tự | Phần | Nguồn | Đổi khi nào |
| --- | --- | --- | --- |
| 1 | Quy tắc chung | `base.md` | Khi sửa prompt |
| 2 | Phần theo vai trò | `role_guest.md`, `role_customer.md`, `role_staff.md`, `role_admin.md` | Khi sửa prompt |
| 3 | Ngữ cảnh của lượt | `context.md.j2`: ngày giờ theo giờ Việt Nam, `page_context` | Mỗi lượt |
| 4 | Nhắc hết lượt tool | Một câu cố định, chỉ khi đã gọi đủ 5 tool (mục 2.7) | Khi cần |

Xếp phần cố định lên trước để các lượt có chung một đoạn đầu giống hệt nhau. Provider nào hỗ trợ prompt caching sẽ tính rẻ và trả nhanh hơn cho đoạn đó, có lợi cho NFR03 và NFR13.

Không dùng ví dụ mẫu (few-shot) trong bản đầu. Quy tắc cùng mô tả tool rõ ràng thường đủ, mà mỗi ví dụ thêm vào đều tốn token ở mọi lượt. Chỉ thêm ví dụ cho đúng lỗi mà bộ đánh giá (mục 7) chỉ ra.

Ước tính (chưa đo) cho một lần gọi model của Customer: system prompt khoảng 700 token, schema 8 tool khoảng 1.200 token, cửa sổ lịch sử tối đa 8.000 token. Tổng input tối đa khoảng 10.000 token.

