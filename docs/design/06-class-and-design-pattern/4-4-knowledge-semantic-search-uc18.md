Nguồn: 06-CLASS-AND-DESIGN-PATTERN.md > Mirra — B6: Thiết kế lớp và design pattern > 4. ai-service > 4.4 Knowledge (tìm kiếm ngữ nghĩa, UC18)
### 4.4 Knowledge (tìm kiếm ngữ nghĩa, UC18)

```mermaid
classDiagram
  class SearchIndexService {
    <<service>>
    +sync(source_type: SourceType, id: UUID) None
    +reindex_all() int
    +search(query: str, filters: SearchFilters, k: int) list~SearchHit~
  }
  class ProductDraftService {
    <<service>>
    +generate(images: list~Upload~, note: str, actor: CurrentUser) ProductDraft
  }
  class IndexSyncConsumer {
    #handle(type: str, data: dict) None
  }
  class StreamConsumer {
    <<abstract>>
  }
  class EmbeddingProvider {
    <<interface>>
    +embed(texts: list~str~) list~list~float~~
    +dimensions: int
  }
  class LLMProvider {
    <<interface>>
  }
  class SearchDocumentRepository {
    <<repository>>
    +upsert(doc: SearchDocument) None
    +remove(source_type: SourceType, id: UUID) None
    +nearest(vector: list~float~, k: int, source_type: SourceType) list~SearchHit~
  }
  class CoreApiClient {
    <<interface>>
  }
  class CostRecorder {
    <<service>>
  }

  StreamConsumer <|-- IndexSyncConsumer
  IndexSyncConsumer --> SearchIndexService
  SearchIndexService --> CoreApiClient
  SearchIndexService --> EmbeddingProvider
  SearchIndexService --> SearchDocumentRepository
  SearchIndexService --> CostRecorder
  ProductDraftService --> LLMProvider
  ProductDraftService --> CoreApiClient
  ProductDraftService --> CostRecorder
```

- `sync` lấy nội dung mới nhất qua `/internal/v1/index-documents`, 404 thì xóa tài liệu, còn lại tạo embedding và upsert; nhận cùng sự kiện hai lần vẫn ra cùng kết quả.
- `search` chỉ trả tài liệu `visible`; agent lấy giá và tồn mới từ core sau đó.
- `ProductDraftService` gọi LLM với structured output, danh mục lấy từ API công khai của core; không lưu gì (B3 mục 3.6).

