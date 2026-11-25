Nguồn: 01-UC.md > Mirra — B1: Phân rã và đặc tả use case > 2. Phân rã use case > 2.1 Quản lý tài khoản
### 2.1 Quản lý tài khoản

```mermaid
flowchart LR
  G((Guest)) --- U01([UC01 Đăng ký tài khoản])
  U01 -. include .-> U011([UC01.1 Xác thực email])
  C((Customer / Staff / Admin)) --- U02([UC02 Đăng nhập, đăng xuất])
  U03([UC03 Quên mật khẩu]) -. extend .-> U02
  CU((Customer)) --- U04([UC04 Quản lý hồ sơ và sổ địa chỉ])
  U04 --> U041([UC04.1 Sửa hồ sơ, đổi mật khẩu])
  U04 --> U042([UC04.2 Thêm, sửa, xóa địa chỉ])
  U04 --> U043([UC04.3 Đặt địa chỉ mặc định])
```

| UC | Quan hệ | Điều kiện, ghi chú | Giai đoạn |
| --- | --- | --- | --- |
| UC01.1 Xác thực email | «include» UC01 | Link hết hạn sau 24 giờ, gửi lại được | MVP |
| UC03 Quên mật khẩu | «extend» UC02 | Khi người dùng bấm "Quên mật khẩu" | Mở rộng |
| UC04.1–UC04.3 | UC con của UC04 | Đặc tả gộp ở mục 4 | MVP |

