# names - class (int, float, list), function (print), constants / variables

X = 100


def func(a):
    b = 10
    # X = 500  # shadows name from outer scope

    def inner(x):
        y = 1
        # a = 100  # shadows name from outer scope

        print('Built-in names:', len, tuple, TypeError, None)
        print('Global names:', X, func)
        print('Enclosing names:', a, b, inner)
        print('Local names:', x, y, end='\n\n')

    inner(2)

    print('Built-in names:', len, tuple, TypeError, None)
    print('Global names:', X, func)
    print('Local names:', a, b, inner, end='\n\n')


func(20)

print('Built-in names:', len, tuple, TypeError, None)
print('Global names:', X, func, end='\n\n')

# int = 0  # shadowing built-in name - not recommended
