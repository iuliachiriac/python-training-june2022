X = 10


def get_long_strings(*args: str, n: int = None):
    """Enter any number of strings, and an optional integer parameter n
    (value defaults to 0 if left unspecified)"""
    if not n:
        return list(args)
    l = []
    for elem in args:
        if len(elem) > n:
            l.append(elem)
    return l


# print(f'The name of the module is {__name__}')
if __name__ == '__main__':
    print(get_long_strings('ceva', 'altceva', n=5))
    print(get_long_strings('', 'altceva'))
