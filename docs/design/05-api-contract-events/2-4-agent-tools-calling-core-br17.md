Nguồn: 05-API-CONTRACT-EVENTS.md > Mirra — B5: API, contract, sự kiện > 2. Xác thực và phân quyền > 2.4 Tool của agent gọi core (BR17)
### 2.4 Tool của agent gọi core (BR17)

- Mỗi request chat hoặc xác nhận hành động đều kèm access token hiện tại của người dùng. ai-service chuyển nguyên token đó sang core qua `CoreApiClient`, không lưu token vào DB hay checkpoint.
- Hành động chờ xác nhận được thực thi bằng token của request xác nhận, nên token cũ hết hạn trong lúc chờ không ảnh hưởng.
- Tool của Guest chỉ gọi endpoint công khai, không kèm token.
- Core kiểm quyền như mọi request khác; agent không có quyền nào hơn người đang chat.

