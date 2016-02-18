from functools import reduce
def prod(L):
    def fu(x,y):
        return x*y
    return reduce(fu,L)
print('1 * 2 * 3 * 4 * 5=',prod([1,2,3,4,5]))


