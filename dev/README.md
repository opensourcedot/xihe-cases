# Developer Contribution Hub

This repository serves as a curation space for innovative implementations before they qualify for promotion to `/platform` directory and public synchronization to [xihe.mindspore.cn](https://xihe.mindspore.cn).


## Purpose 🎯
- **Incubation Space**: Validate experimental implementations in a staging environment
- **​Quality Gateway**: Ensure architectural consistency before production promotion
- **Knowledge Repository**: Aggregate community-driven innovations with version traceability


## Contribution Guidelines ✍️

### 1. Directory Hierarchy Specification
```plaintext
dev/
├── ascend/
│   ├── snt9/                      # Hardware-specific implementations
│   │   ├── 2_5/                   # MindSpore version (major_minor)
│   │   │   └── images/            # Your images folder
│   │   │   └── <new_case>         # Your case
│   │   └── <new_mindspore_version> # Future version support
└── cpu/                           # Generic CPU implementations     
    ├── 2_5/                       # MindSpore version (major_minor)                       
    │   └── <new_case>
    └── <new_mindspore_version>
```