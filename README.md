# homework-line

基于 GitHub Actions 的 Python 单元测试持续集成（CI）示例项目。

![Python单元测试](https://github.com/dusk5-Surtr/homework-line/actions/workflows/ci.yml/badge.svg?branch=main)

## 项目简介

本仓库演示如何为一个 Python 项目配置测试环境，并用 GitHub Actions 在每次
`push` / `pull_request` 时自动运行单元测试。

`calculator.py` 是被测试的功能模块（加、减、乘、除），`test_calculator.py`
是使用 `pytest` 编写的单元测试。

## 目录结构

```
homework-line/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions 工作流：自动运行单元测试
├── calculator.py           # 被测试的代码
├── test_calculator.py      # 测试代码
├── requirements.txt        # 项目依赖
├── .gitignore
└── README.md
```

## 本地运行测试

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 运行测试（-v 显示每个用例的详细结果）
pytest -v
```

预期输出：

```
test_calculator.py::test_add PASSED
test_calculator.py::test_subtract PASSED
test_calculator.py::test_multiply PASSED
test_calculator.py::test_divide PASSED
test_calculator.py::test_divide_by_zero PASSED

============================== 5 passed ==============================
```

## 持续集成工作流

`.github/workflows/ci.yml` 在推送代码时自动执行四个步骤：

| 步骤 | 作用 |
|---|---|
| **检出代码** | `actions/checkout@v4` 把仓库代码取到运行器中 |
| **设置Python** | `actions/setup-python@v5` 配置 Python 3.11 环境 |
| **安装依赖** | 升级 pip 并安装 `pytest` |
| **运行测试** | 执行 `pytest -v`，输出每个用例的详细结果 |

## 如何判断测试结果

- **测试通过** ✅：Actions 页面对勾，日志末尾显示 `5 passed`
- **测试失败** ❌：Actions 页面红叉，日志中会指出失败的用例名与断言差异

例如把 `add()` 改成 `return a * b`（错误实现）后推送，工作流会立刻变红，
`test_add` 报 `assert 6 == 5`，从而在合并前就拦截住这个缺陷。
