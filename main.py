
def func_gen():
    n = open('text.txt', encoding='utf-8')
    d = {}
    for line in n:
        key, *value = line.split()
        d[key] = value
        korteg = tuple([d])

        for i in [korteg]:
            yield i

    n.close()
    #yield korteg

a = func_gen()
print(next(a))
print(next(a))
print(next(a))











