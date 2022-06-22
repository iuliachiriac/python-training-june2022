def decrement(nr, step=1):
    return nr - step


# call with required argument
result = decrement(100)
print(result)

# call with required argument & specify value for optional argument
result = decrement(100, 2)
print(result)

# call with keyword arguments
result = decrement(100, step=3)
print(result)

result = decrement(nr=100, step=4)
print(result)


def varargs(*args, **kwargs):
    print(args, type(args), len(args))
    print(kwargs, type(kwargs), len(kwargs), end="\n\n")


varargs()
varargs(10)
varargs(10, 20, 30, 'hello')
varargs(hello=10)
varargs(10, 20, 30, hello=1, hi=5)


def all_parameters_types(pos1, pos2, *pos, req_kw, kw1=None, kw2=0, **kwargs):
    print(pos1, pos2, pos, req_kw, kw1, kw2, kwargs)


all_parameters_types(1, 2, req_kw='test')
all_parameters_types(1, 2, 3, 4, 5, 6, req_kw='test', kw1='value', kw7='xx')
