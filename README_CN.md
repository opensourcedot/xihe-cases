\[ [English](README.md) | 中文 \]
## 🚀 简介
本仓库收集了一系列基于 MindSpore 框架的教育与训练案例，旨在为 [昇思大模型平台](https://xihe.mindspore.cn/) 平台上的 AI 学习与模型实验提供实践支持。

无论你是 AI 初学者，还是有经验的开发者，这些案例都可以帮助你动手构建、训练和部署模型，深入理解 AI 技术。

## 🧠 特性
* 简明易懂的 MindSpore 教学与实战案例
* 与 [昇思大模型平台](https://xihe.mindspore.cn/) 高度兼容，无需本地环境配置
* 支持 Ascend 和 CPU 双平台
* 持续维护，欢迎社区贡献

## 📦 支持平台与版本
| 平台 | 支持的 MindSpore 版本 |
|----------|------------------------------|
| Ascend   | 2_5, 2_4, 2_3, 2_2           |
| CPU      | 2_5, 2_4, 2_3                |

> ℹ️ 案例按平台和版本分类整理，并持续更新以支持 MindSpore 的新版本。

## 📁 仓库结构
```plaintext
xihe-cases/
├── dev/                            # 社区贡献案例
│   ├── ascend/                     # Ascend 平台案例
│   ├── cpu/                        # CPU 平台案例
│   ├── README.md                   # 英文贡献指南
│   └── README_CN.md                # 中文贡献指南
├── platform/                       # 官方维护案例
│   ├── ascend/                     # Ascend 平台案例
│   └── cpu/                        # CPU 平台案例  
├── LICENSE                         # 开源许可证
├── README.md                       # 英文文档
└── README_CN.md                    # 中文文档
```

## 💡 快速开始
你可以直接在 [昇思大模型平台](https://xihe.mindspore.cn/) 上运行案例，无需本地安装。
如需在本地运行：

1. 安装 MindSpore
请根据你的平台参考 MindSpore 安装指南。

2. 克隆仓库
```bash
git clone https://github.com/opensourcedot/xihe-cases.git
cd xihe-cases
```
3. 运行案例
进入任意案例目录，根据其中的案例进行操作。

## 🤝 开发者贡献中心
我们欢迎社区开发者参与贡献！如果你创建了有价值的案例，可以将其提交至 **dev/** 目录。

📘 详情请参考[开发者贡献中心](dev/README_CN.md)

## 许可证
本项目基于 Apache License 2.0 开源发布。
