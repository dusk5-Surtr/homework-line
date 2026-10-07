"""calculator 模块的单元测试，由 GitHub Actions 自动执行。"""

import pytest

from calculator import add, divide, multiply, subtract


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 7) == -7


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(2, 0) == 0


def test_divide():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
