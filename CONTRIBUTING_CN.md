# xihe-cases 贡献指南

欢迎投稿，非常感谢！每一点帮助都有作用，功劳也总是会被认可的。

## 贡献类型

### 报告 Bugs
如果您发现了 Bug，请在 https://github.com/opensourcedot/xihe-cases/issues 提交问题。

如果您要报告bug，请包括：

* 您的实验环境和版本。

    - 硬件环境（如，Ascend NPU）
    - MindSpore 版本（如，MindSpore 2.5.0）
    - Python 版本（如, Python 3.9.21）
    - 操作系统（如, Python 3.9.21）

* 可能有助于排查问题的本地环境细节。
* 重现 Bug 的详细步骤。

### 提交反馈
发送反馈的最佳方式是向 https://github.com/opensourcedot/xihe-cases/issues 提交问题。

如果您提出的是一个新功能或新案例：

* 详细说明它如何工作。
* 请记住，这是一个由志愿者推动的项目，欢迎任何贡献 :)

## 开始贡献

准备好贡献了吗？以下是为本地开发设置 `xihe-cases`的方法。

### 1. Fork 仓库
在 [GitHub](https://github.com/opensourcedot/xihe-cases) 上 Fork `xihe-cases` 仓库。

### 2. 克隆您的 Fork
将仓库克隆到本地机器：
```bash
git clone git@github.com:YOUR_USERNAME/xihe-cases.git
```

然后，添加官方仓库作为上游仓库：
```bash
git remote add upstream git@github.com:opensourcedot/xihe-cases
```

### 3. 创建一个新分支
在进行任何修改之前，先为您的功能或 Bug 修复创建一个新分支：
```bash
git checkout -b name-of-your-bugfix-or-feature
```

### 4. 进行修改
根据需要修改代码库。在修改时，请确保：

* 遵循项目的编码风格和约定。
* 编写有意义的提交信息。
* 必要时添加或修改测试。
* 如果您的修改影响到功能或用户界面，更新相关文档。

### 5. 测试您的修改
在提交修改之前，请确保一切按预期工作。如有可能，在 [xihe.mindspore.cn](https://xihe.mindspore.cn) 平台上测试您的修改。

### 6. 提交您的修改
```bash
git add .
git commit -m "feat(fix): 您对修改的详细描述。"
git push origin name-of-your-bugfix-or-feature
```
### 7. 提交 Pull Request
当您的修改准备好后，向主仓库提交 Pull Request（PR）。在提交 PR 时，请提供以下信息：

**PR 标题**

保持简洁，并遵循以下格式： [类型] - 简短描述。

- [Feat] 新增...(如：壁画修复)案例
- [Fix] 修复关于...的 Bug
- [Docs] 更新文档...

**PR 描述**

提供关于您修改的详细信息，包括动机、测试以及相关问题。
