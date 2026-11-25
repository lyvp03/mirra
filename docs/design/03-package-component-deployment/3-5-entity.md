Nguồn: 03-PACKAGE-COMPONENT-DEPLOYMENT.md > Mirra — B3: Package, Component, Deployment > 3. Ánh xạ lớp B2 vào package > 3.5 Entity
### 3.5 Entity

| Schema | Entity | Lưu file |
| --- | --- | --- |
| `core` (core\_api) | User, AuthToken, Address, AdminUnit, Category, SizeChart, Product, ProductVariant, ProductImage, Promotion, Cart, CartItem, Order, OrderItem, OrderStatusHistory, Payment, InventoryLedgerEntry, Review, Faq, Setting, SettingHistory | Ảnh sản phẩm ở bucket `products` |
| `ai` (ai\_service) | PhotoConsent, UserPhoto, TryOnJob, WebcamSession, WebcamBudget, Conversation, ChatMessage, PendingAction, OutfitSuggestion, SearchDocument, AICostRecord | Ảnh người dùng, kết quả try-on, video, khung hình webcam ở bucket `tryon` |

Quan hệ cắt ngang hai schema ở B2 (TryOnJob → ProductVariant, AICostRecord → …, Conversation → User) lưu dạng ID tham chiếu, không có khóa ngoại giữa hai schema; tính đúng đắn do API của core đảm bảo.

