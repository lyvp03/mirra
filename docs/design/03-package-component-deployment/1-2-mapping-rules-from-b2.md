Nguồn: 03-PACKAGE-COMPONENT-DEPLOYMENT.md > Mirra — B3: Package, Component, Deployment > 1. Quy ước và quyết định > 1.2 Quy tắc ánh xạ từ B2
### 1.2 Quy tắc ánh xạ từ B2

| Lớp B2 | Đích trong thiết kế |
| --- | --- |
| Boundary giao diện (Screen, Form, Widget, Dialog, Card) | Trang và component của web (Next.js) |
| Boundary hệ thống ngoài (`...Boundary`) | Adapter trong tầng `adapters` của service sở hữu, sau một interface |
| Control theo UC (`...Controller`) | Service nghiệp vụ trong tầng `services`; các control cùng chủ đề gộp vào một service |
| Control dùng chung (`Policy`, `Calculator`, `StateMachine`, `Validator`, `Composer`) | Tầng `domain` của service sở hữu |
| Entity | Model ORM trong tầng `models`, thuộc schema `core` hoặc `ai` |
| SchedulerBoundary | Job định kỳ trong core-worker hoặc ai-worker |

