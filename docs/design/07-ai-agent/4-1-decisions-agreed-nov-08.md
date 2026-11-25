Nguồn: 07-AI-AGENT.md > Mirra — B7: Thiết kế AI agent > 4. Tool > 4.1 Quyết định đã chốt (08/11)
### 4.1 Quyết định đã chốt (08/11)

| Vấn đề | Chốt |
| --- | --- |
| Tool ghi của Customer | Chỉ `add_to_cart`; hủy đơn vẫn làm ở trang đơn hàng |
| Tool ghi của Staff/Admin | Chỉ `update_order_status`; chỉnh tồn làm ở trang quản trị |
| Viết nháp sản phẩm từ ảnh | Chỉ là nút trên form sản phẩm (`ProductDraftService` của B6), **bỏ khỏi danh sách tool chat**; API chat vẫn chỉ nhận text |
| Cách tìm sản phẩm | Tìm vector ở ai, rồi core lọc và trả giá, tồn hiện tại |

