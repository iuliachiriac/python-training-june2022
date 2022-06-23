def make_pretty(func):  # func is the decorated function before decoration
    def inner(*args, **kwargs):
        print("I got decorated")
        result = func(*args, **kwargs)
        return result
    return inner


@make_pretty
def ordinary():
    print("I am ordinary")


@make_pretty
def greet(name):
    print(f'Hello, {name}!')


@make_pretty
def add(a, b):
    return a + b


# print('Before decoration:', ordinary)
# ordinary()
# ordinary = make_pretty(ordinary)  # ordinary becomes make_pretty.<locals>.inner

print('After decoration:', ordinary)
ordinary()

greet('John')

print('Add result:', add(10, 20))


# def greet(name):
#     print(f'Hello, {name}!')
#
#
# greet('John')
#
# salute = greet
# salute('Anna')
#
#
# def add(a, b):
#     return a + b
#
#
# def diff(a, b):
#     return a - b
#
#
# def get_operation(operator):
#     if operator == '+':
#         return add
#     else:
#         return diff
#
#
# func = get_operation('+')
# print(func(10, 20))
#
# func = get_operation('-')
# print(func(10, 20))
