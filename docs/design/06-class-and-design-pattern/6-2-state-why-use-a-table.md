Nguồn: 06-CLASS-AND-DESIGN-PATTERN.md > Mirra — B6: Thiết kế lớp và design pattern > 6. Design pattern > 6.2 State — vì sao dùng bảng
### 6.2 State — vì sao dùng bảng

GoF nêu State có thể cài bằng mỗi trạng thái một lớp, hoặc bằng bảng ánh xạ (trạng thái, sự kiện) → trạng thái mới. Mirra chọn bảng vì 8 trạng thái chỉ khác nhau ở chỗ được chuyển đi đâu, ai được chuyển và hành động phụ; không có hành vi riêng nào khác để đặt vào từng lớp. Bảng ở mục 3.3.1 vừa là code, vừa sinh được sơ đồ trạng thái, và test được toàn bộ bằng một test tham số hóa qua mọi cặp (từ, đến, vai trò). Khi trình bày trong báo cáo: Context = `Order`, State = dòng bảng của trạng thái hiện tại, transition = `OrderStateMachine.transition`.

Các vòng đời nhỏ hơn (`TryOnJob`, `WebcamSession`, `PendingAction`) dùng cùng cách: một bảng chuyển hợp lệ trong lớp domain của component.

