"""calculator: 一个用来演示单元测试与持续集成的简单计算器模块。"""


def add(a, b):
    """返回 a 与 b 的和。"""
    return a + b


def subtract(a, b):
    """返回 a 与 b 的差。"""
    return a - b


def multiply(a, b):
    """返回 a 与 b 的积。"""
    return a * b


def divide(a, b):
    """返回 a 除以 b 的商；b 为 0 时抛出 ZeroDivisionError。"""
    if b == 0:
        raise ZeroDivisionError("除数不能为 0")
    return a / b


if __name__ == "__main__":
    print("2 + 3 =", add(2, 3))
    print("3 * 4 =", multiply(3, 4))
