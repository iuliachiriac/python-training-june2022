greeting = input('greeting = ')
idx = 0

print(greeting)

try:
    char = greeting[idx]
    if char.isupper():
        raise ValueError
except IndexError as e:
    print('exception caught:', e)
except ValueError:
    pass
else:
    print('no exception occurred')
finally:
    print('executes every time')
