import json
from pathlib import Path

massive_taxonomy = {
  "version": "1.0.0",
  "last_updated": "2026-06-15T00:00:00Z",
  "categories": {
    "software_architecture": {
      "weight": 1.0,
      "concepts": {
        "design_patterns": ["singleton", "factory", "abstract factory", "builder", "prototype", "adapter", "bridge", "composite", "decorator", "facade", "flyweight", "proxy", "chain of responsibility", "command", "interpreter", "iterator", "mediator", "memento", "observer", "state", "strategy", "template method", "visitor", "dependency injection", "inversion of control", "mvc", "mvp", "mvvm", "repository", "unit of work", "cqrs", "event sourcing", "saga", "circuit breaker", "bulkhead", "strangler fig", "sidecar", "bff", "api gateway"],
        "principles": ["solid", "single responsibility", "open-closed", "liskov substitution", "interface segregation", "dependency inversion", "dry", "kiss", "yagni", "boy scout rule", "law of demeter", "separation of concerns"],
        "styles": ["microservices", "monolith", "serverless", "event-driven", "soa", "hexagonal architecture", "clean architecture", "onion architecture", "domain-driven design", "ddd"]
      }
    },
    "languages": {
      "weight": 0.9,
      "concepts": {
        "backend": ["python", "java", "c#", "csharp", "c++", "cpp", "go", "golang", "rust", "ruby", "php", "elixir", "erlang", "scala", "haskell", "clojure", "zig", "nim", "mojo", "dart"],
        "frontend": ["javascript", "typescript", "html", "html5", "css", "css3", "sass", "less", "wasm", "webassembly"],
        "scripting": ["bash", "shell", "powershell", "perl", "lua", "awk", "sed"],
        "data": ["sql", "pl/sql", "t-sql", "r", "julia", "matlab"]
      }
    },
    "web_frameworks": {
      "weight": 0.8,
      "concepts": {
        "frontend": ["react", "vue", "angular", "svelte", "solidjs", "nextjs", "nuxt", "gatsby", "htmx", "qwik", "ember", "backbone", "lit", "alpine"],
        "backend": ["django", "flask", "fastapi", "fastapi", "spring boot", "asp.net", "express", "nest", "nestjs", "laravel", "ruby on rails", "gin", "fiber", "echo", "actix", "rocket", "axum", "phoenix"]
      }
    },
    "infrastructure_devops": {
      "weight": 0.9,
      "concepts": {
        "containers": ["docker", "podman", "containerd", "kubernetes", "k8s", "k3s", "k0s", "minikube", "docker swarm", "nomad", "mesos", "helm", "kustomize"],
        "iac": ["terraform", "opentofu", "pulumi", "cloudformation", "ansible", "chef", "puppet", "saltstack", "packer", "vagrant", "bicep"],
        "ci_cd": ["github actions", "gitlab ci", "jenkins", "circleci", "travis ci", "bamboo", "teamcity", "argocd", "flux", "tekton", "spinnaker", "drone", "waypoint"],
        "observability": ["prometheus", "grafana", "datadog", "jaeger", "opentelemetry", "fluentd", "zipkin", "elk", "elastic", "logstash", "kibana", "splunk", "new relic", "datadog", "dynatrace"]
      }
    },
    "databases_storage": {
      "weight": 0.9,
      "concepts": {
        "relational": ["postgresql", "mysql", "sqlite", "mariadb", "oracle", "sql server", "cockroachdb", "tidb", "yugabyte"],
        "nosql": ["mongodb", "cassandra", "couchdb", "dynamodb", "firebase", "cosmosdb", "neo4j", "arangodb", "redis", "memcached", "valkey", "dragonfly", "couchbase", "riak"],
        "messaging": ["kafka", "rabbitmq", "activemq", "pulsar", "nats", "zeromq", "sqs", "sns", "eventgrid", "service bus"]
      }
    },
    "artificial_intelligence": {
      "weight": 1.0,
      "concepts": {
        "frameworks": ["pytorch", "tensorflow", "keras", "scikit-learn", "jax", "huggingface", "transformers", "diffusers", "langchain", "llamaindex", "haystack", "vllm", "ollama", "mlx", "tensorrt"],
        "concepts": ["llm", "rag", "retrieval augmented generation", "fine-tuning", "lora", "qlora", "peft", "quantization", "gguf", "ggml", "awq", "gptq", "embeddings", "vector database", "agentic", "chain of thought", "few-shot", "zero-shot", "prompt engineering"],
        "vector_dbs": ["milvus", "qdrant", "weaviate", "pinecone", "chroma", "pgvector"]
      }
    },
    "security": {
      "weight": 0.9,
      "concepts": {
        "auth": ["oauth2", "oidc", "saml", "jwt", "jwe", "mfa", "2fa", "sso", "rbac", "abac", "pbac", "fido2", "webauthn"],
        "crypto": ["tls", "ssl", "aes", "rsa", "ecc", "sha-256", "argon2", "bcrypt", "scrypt", "pki", "x.509"],
        "appsec": ["owasp", "cors", "csrf", "xss", "sqli", "ssrf", "sast", "dast", "sca", "csp"]
      }
    },
    "game_development": {
      "weight": 0.8,
      "concepts": {
        "engines": ["godot", "unity", "unreal", "bevy", "defold", "monogame", "phaser", "libgdx"],
        "concepts": ["ecs", "entity component system", "kinematics", "rigidbody", "raycast", "navmesh", "pathfinding", "state machine", "behavior tree", "shader", "hlsl", "glsl"]
      }
    }
  }
}

with open("taxonomy.json", "w") as f:
    json.dump(massive_taxonomy, f, indent=2)
print("Taxonomy successfully seeded with massive knowledge base.")
