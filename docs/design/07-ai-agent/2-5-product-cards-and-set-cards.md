Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 2. State của agent > 2.5 Thẻ sản phẩm và thẻ set
### 2.5 Thẻ sản phẩm và thẻ set

1. Tool đặt dữ liệu thẻ vào `ToolMessage.artifact`.
2. Khi tool chạy xong, `AgentRunner` phát sự kiện `card.products` hoặc `card.outfit` (B5 mục 5.2) và gom thẻ của lượt đó lại.
3. Khi trả lời xong, `AgentRunner` lưu tin ASSISTANT kèm `cards` (JSONB, danh sách thẻ theo thứ tự xuất hiện).

Thẻ là ảnh chụp tại lúc trả lời. Khi mở lại hội thoại, giá trên thẻ có thể đã khác. Không sao, vì bấm thẻ sẽ mở trang sản phẩm với giá hiện tại, còn thêm vào giỏ và đặt hàng luôn lấy giá từ core (BR04). Thẻ set mang `outfit_id` (trùng `outfit_suggestions.id`, dùng khi thử cả set) và nội dung các set, đúng như sự kiện `card.outfit` của B5, nên SSE và cột `cards` dùng chung một dạng thẻ. Cấu trúc chi tiết của từng loại thẻ ở mục 4.3.

