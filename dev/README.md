# Developer Contribution Hub

This repository serves as a curation space for innovative implementations before they qualify for promotion to `/platform` directory and public synchronization to [xihe.mindspore.cn](https://xihe.mindspore.cn).


## Purpose 🎯
- **Incubation Space**: Validate experimental implementations in a staging environment
- **Quality Gateway**: Ensure architectural consistency before production promotion
- **Knowledge Repository**: Aggregate community-driven innovations with version traceability


## Contribution Guidelines ✍️

### Directory Hierarchy Specification
```plaintext
dev/
├── ascend/
│   │   ├── 2_5/                   # MindSpore version (major_minor)
│   │   │   └── <new_case>         # Your case
│   │   └── <new_mindspore_version> # Future version support
└── cpu/                           # Generic CPU implementations     
    ├── 2_5/                       # MindSpore version (major_minor)                       
    │   └── <new_case>
    └── <new_mindspore_version>
```

### General Contribution Requirements
To ensure high-quality contributions, please adhere to the following guidelines:

* Image Usage:
  * Avoid storing images in the repository to reduce its size.
  * Use online links to embed images directly into the introductory documentation.
  * Prevent `notebook` files from bloating by avoiding `plt.show()` or similar methods to embed image data.
  * Keep files concise to improve review efficiency.
* Dependencies:
  * Include the mindspore installation script to allow seamless execution in other environments.
  * Ensure all required dependencies at the beginning of case for easy installation.
* Code Quality:
  * Provide a brief introduction for any network models included, explaining their purpose and structure.
  * Add clear and meaningful comments to explain the code logic.
  * Keep output concise and relevant to the tutorial or example.
* Pull Request (PR) Submission:
  * Include a detailed description of the changes made in the PR.
  * Provide a test report in the PR description, including the test environment, runtime, and performance metrics.

If you need further assistance with formatting or additional guidelines, feel free to open an issue.
