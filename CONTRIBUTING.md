# xihe-cases Contributing Guidelines

Contributions are welcome, and they are greatly appreciated! Every little
helps, and credit will always be given.

## Types of Contributions

### Report Bugs

Report bugs at https://github.com/opensourcedot/xihe-cases/issues.

If you are reporting a bug, please include:

* Your experimental environment and version.

    - Hardware Environment (e.g., Ascend NPU)
    - MindSpore version (e.g., MindSpore 2.5.0)
    - Python version (e.g., Python 3.9.21)
    - OS platform (e.g., openEuler 22.03)

* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Submit Feedback

The best way to send feedback is to file an issue at https://github.com/opensourcedot/xihe-cases/issues.

If you are proposing a feature or new case:

* Explain in detail how it would work.
* Remember that this is a volunteer-driven project, and that contributions are welcome :)

## Getting Started

Ready to contribute? Here's how to set up `xihe-cases` for local development.

### 1. Fork the Repository
Fork the `xihe-cases` repo on [GitHub](https://github.com/opensourcedot/xihe-cases).

### 2. Clone Your Fork
Clone the repository to your local machine:
```bash
git clone git@github.com:YOUR_USERNAME/xihe-cases.git
```

After that, you should add official repository as the upstream repository:
```bash
git remote add upstream git@github.com:opensourcedot/xihe-cases
```

### 3. Create a New Branch
Before making any changes, create a new branch for your feature or bug fix:
```bash
git checkout -b name-of-your-bugfix-or-feature
```

### 4. Make Your Changes
Make the necessary changes to the codebase. When doing so, please ensure that you:

* Follow the project's coding style and conventions.
* Write meaningful commit messages.
* Add or modify tests if necessary.
* Update relevant documentation if your changes affect the functionality or user-facing aspects.

### 5. Test Your Changes
Before submitting your changes, ensure everything works as expected. If applicable, test your changes on the [xihe.mindspore.cn](https://xihe.mindspore.cn) platform.

### 6. Commit Your Changes
```bash
git add .
git commit -m "feat(fix): Your detailed description of your changes."
git push origin name-of-your-bugfix-or-feature
```

### 7. Submit a Pull Request
Once your changes are ready, open a pull request (PR) to the main repository. Please provide the following in your PR:

**PR Title**

Keep it concise and follow the format: [Type] - Short description.
- [Feat] Added ...(e.g., mural restoration) case
- [Fix] Fix bug about...
- [Docs] Update document...

**PR Description**

Provide detailed information about your changes, including motivation, testing, and any related issues.
