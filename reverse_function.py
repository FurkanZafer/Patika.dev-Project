list_ = [[1, 2], [3, 4], [5, 6, 7]]

def rev(n):
    n.reverse()
    for i in n:
        if type(i) == list:
            i.reverse()
    
rev(list_)    
print(list_)