Nguồn: 03-PACKAGE-COMPONENT-DEPLOYMENT.md > Mirra — B3: Package, Component, Deployment > 5. Sơ đồ deployment > 5.1 Production
### 5.1 Production

```mermaid
flowchart TB
  USER["«device» User browser"]
  DEV["«device» Developer machine"]
  subgraph CI["«execution environment» GitHub"]
    GHA["GitHub Actions<br/>lint, test, build"]
    REG[("GHCR<br/>web, core, ai images")]
  end
  subgraph VPS["«node» VPS: Linux, Docker Engine, Compose"]
    CADDY["«container» caddy<br/>ports 80, 443 published"]
    subgraph APPS["application containers"]
      WEB["«container» web<br/>:3000"]
      CORE["«container» core-api<br/>:8000"]
      AI["«container» ai-service<br/>:8001"]
      CW["«container» core-worker"]
      AW["«container» ai-worker"]
    end
    subgraph DATA["data containers"]
      PG[("«container» postgres<br/>pgvector, :5432")]
      RD[("«container» redis<br/>:6379")]
      S3[("«container» minio<br/>:9000")]
    end
    JG["«container» jaeger<br/>OTLP :4317, UI :16686"]
  end
  subgraph SAAS["«external» SaaS"]
    EXT["payOS, SMTP provider,<br/>LLM and embedding providers,<br/>try-on provider, Langfuse Cloud"]
    RT["realtime try-on provider"]
  end
  USER -->|"HTTPS 443"| CADDY
  CADDY -->|"/"| WEB
  CADDY -->|"/api"| CORE
  CADDY -->|"/ai"| AI
  CADDY -->|"media subdomain"| S3
  APPS -->|"SQL, Redis, S3 API"| DATA
  APPS -.->|OTLP| JG
  APPS -->|"HTTPS egress"| EXT
  EXT -->|"webhooks via caddy"| CADDY
  USER -.->|WebRTC| RT
  GHA --> REG
  GHA -->|"SSH: pull, migrate, up"| VPS
  REG -.->|docker pull| VPS
  DEV -.->|"SSH tunnel to Jaeger UI"| JG
```

10 container trên một VPS, chỉ Caddy mở cổng ra ngoài. Webhook của payOS và try-on provider đi vào qua Caddy như mọi request khác.

