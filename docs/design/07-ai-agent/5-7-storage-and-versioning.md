Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 5. Prompt > 5.7 Lưu và quản lý phiên bản
### 5.7 Lưu và quản lý phiên bản

```text
ai_service/agent/prompts/
  base.md
  role_guest.md
  role_customer.md
  role_staff.md
  role_admin.md
  context.md.j2
  guardrail_classifier.md
  outfit_suggester.md   # prompt của OutfitService (B6)
```

- `prompt_version` = 8 ký tự đầu của SHA-256 trên `base.md` + file vai trò. Giá trị này ghi vào metadata của mỗi trace Langfuse, nên nhìn trace là biết câu trả lời đến từ bản prompt nào.
- Sửa prompt = một commit. Trước khi merge phải chạy bộ đánh giá ở mục 7 và so với bản trước.
- Prompt nạp một lần khi ai-service khởi động, không đọc file ở mỗi request.

