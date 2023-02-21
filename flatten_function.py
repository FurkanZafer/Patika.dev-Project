list_ = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
m = []


def flatten(list_):
    for i in list_:
        is_list(i)


def is_list(n):
    if type(n) == list:
        flatten(n)
    else:
        m.append(n)


flatten(list_)

print(m)