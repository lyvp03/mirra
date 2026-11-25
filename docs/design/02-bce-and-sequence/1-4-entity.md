Nguồn: 02-BCE-AND-SEQUENCE.md > Mirra — B2: Phân tích BCE và sequence > 1. Quy ước và danh mục lớp phân tích > 1.4 Entity
### 1.4 Entity

| Lớp | Mô tả |
| --- | --- |
| User | Tài khoản: vai trò, trạng thái xác thực, trạng thái khóa |
| AuthToken | Token xác thực email, đặt lại mật khẩu, refresh token |
| Address | Địa chỉ giao hàng 2 cấp trong sổ địa chỉ |
| AdminUnit | Tỉnh/Thành, Phường/Xã và tọa độ tâm |
| Category, SizeChart | Danh mục và bảng size theo danh mục |
| Product | Sản phẩm: tên thương mại, tên mô tả tiếng Việt, mô tả, loại món, trạng thái, giá gốc |
| ProductVariant | SKU màu × size, tồn kho |
| ProductImage | Ảnh người mẫu và ảnh flat-lay (tùy chọn) theo màu, cờ bật thử đồ, mô tả trang phục |
| Promotion | Giá khuyến mãi có khoảng ngày |
| Cart, CartItem | Giỏ hàng trên server |
| Order, OrderItem | Đơn hàng, dòng đơn với giá lúc đặt; thông tin người nhận, token tra đơn cho Guest |
| OrderStatusHistory | Lịch sử đổi trạng thái |
| Payment | Thanh toán: phương thức, trạng thái, mã giao dịch, mã hoàn tiền |
| InventoryLedgerEntry | Dòng sổ kho |
| Review | Đánh giá sản phẩm |
| Faq | Bài FAQ, chính sách song ngữ |
| Setting, SettingHistory | Cấu hình hệ thống và lịch sử thay đổi |
| PhotoConsent | Log đồng ý xử lý ảnh, phiên bản điều khoản |
| UserPhoto | Ảnh toàn thân của khách |
| TryOnJob | Một lượt thử đồ ảnh hoặc video: món/set, trạng thái, kết quả |
| WebcamSession | Phiên webcam: thời điểm, số giây dùng |
| WebcamBudget | Trần ngân sách webcam toàn hệ thống, số giây còn lại |
| Conversation, ChatMessage | Hội thoại với trợ lý và tin nhắn |
| PendingAction | Thao tác ghi đang chờ người dùng xác nhận |
| OutfitSuggestion | Set phối đồ đã gợi ý (món trên, món dưới, lý do) |
| SearchDocument | Nội dung sản phẩm, FAQ đã lập chỉ mục tìm kiếm ngữ nghĩa |
| AICostRecord | Chi phí mỗi lần gọi dịch vụ AI |

