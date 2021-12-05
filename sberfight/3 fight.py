import collections


def get_result1(numb):
    d = dict()
    for n in numb:
        if n in d:
            d[n] += 1
        else:
            d[n] = 1
    d = sorted(d.items(), key=lambda x: x[0])
    c = [z for z in d if z[1] % 2 != 0]
    return False if len(c) > 1 else True


def get_result2(numb):
    c = list(collections.Counter(numb).items())
    r = [z for z in c if z[1] % 2 != 0]
    return False if len(r) > 1 else True
