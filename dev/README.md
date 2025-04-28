# Developer Contribution Hub

This repository serves as a curation space for innovative implementations before they qualify for promotion to `/platform` directory and public synchronization to [xihe.mindspore.cn](https://xihe.mindspore.cn).


## Purpose 🎯
- **Incubation Space**: Validate experimental implementations in a staging environment
- **​Quality Gateway**: Ensure architectural consistency before production promotion
- **Knowledge Repository**: Aggregate community-driven innovations with version traceability


## Contribution Guidelines ✍️

### Directory Hierarchy Specification
```plaintext
dev/
├── ascend/
│   ├── snt9/                      # Hardware-specific implementations
│   │   ├── 2_5/                   # MindSpore version (major_minor)
│   │   │   └── <new_case>         # Your case
│   │   └── <new_mindspore_version> # Future version support
└── cpu/                           # Generic CPU implementations     
    ├── 2_5/                       # MindSpore version (major_minor)                       
    │   └── <new_case>
    └── <new_mindspore_version>
```
​To enhance clarity and reduce ambiguity in the contribution guidelines, especially regarding image usage in tutorials, consider updating the note as follows:​

> Note: When incorporating images into tutorials, please ensure they are embedded directly within the document using online links. This practice minimizes ambiguity and enhances clarity.​

If you need further assistance with formatting or additional guidelines, feel free to open an issue.