def add(*args):
    res = 0
    for n in args:
        res += n
    return res


print(add(1,2,3,4,5))