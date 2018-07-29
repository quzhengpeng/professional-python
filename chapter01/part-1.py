# 装饰器类
def decorated_bu(func):
    func.__doc__ += '\nDecorated by decorated_by.'
    return func


# 将装饰器函数运用到 add() 函数的示例
def add(x, y):
    """Return the sum of x and y."""
    return x + y


add = decorated_bu(add)

print(add.__doc__)
print()


# 将装饰器函数运用到 add() 函数的特殊语法
@decorated_bu
def add(x, y):
    """Return the sum of x and y."""
    return x + y


print(add.__doc__)
print()


# 使用两个装饰器
def also_decorated_by(func):
    func.__doc__ += "\nDecorated by also_decorated_by."
    return func


@also_decorated_by
@decorated_bu
def add(x, y):
    """Return the sum of x and y."""
    return x - y


print(add.__doc__)
