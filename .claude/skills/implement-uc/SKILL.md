---
name: implement-uc
description: Plan, then implement one Mirra use case from the split design docs
disable-model-invocation: true
arguments: [uc, mode]
argument-hint: "[mã UC] [code]"
---
UC: $uc. Chế độ: "$mode" (rỗng = lập plan; "code" = viết code theo plan đã duyệt).

## Chế độ lập plan
1. Dùng subagent Explore: đọc dòng $uc trong docs/design/INDEX.md, rồi chỉ mở các file nhỏ được trỏ tới. Trả về trích đoạn cần để code, tối đa khoảng 150 dòng. Session chính không tự mở tài liệu thiết kế.
2. Viết docs/plans/$uc.md, đủ để code mà không phải mở lại thiết kế: file tạo/sửa, chữ ký hàm (B6), cột và ràng buộc (B4), endpoint và mã lỗi (B5), ca test kèm mã ca (B9), điểm còn mơ hồ.
3. DỪNG: tóm tắt plan trong 10 dòng, chờ tôi duyệt.

## Chế độ code (tôi đã /clear trước khi gọi)
4. Chỉ đọc docs/plans/$uc.md và code liên quan. Thiếu chi tiết thiết kế thì mở đúng một file nhỏ qua INDEX, không mở cả thư mục.
5. Viết test trước, chạy cho thấy test đỏ.
6. Viết code tới khi test xanh. Không đổi tên lớp, endpoint, mã lỗi khác plan; buộc phải lệch thì DỪNG và hỏi.
7. Chạy ruff, lint-imports, pytest unit + integration của service. Dán output cuối.
8. Báo cáo: file đã đổi, ca test đã phủ, chỗ lệch thiết kế, 3 đoạn code tôi nên đọc kỹ và vì sao.
