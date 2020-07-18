'''
Finding the nth Fibonacci number
'''

def fibo(_n):
    '''
    Fibonacci numbers
    '''
    _a, _b = 0, 1

    # for block - 10/10
    for _i in range(1, _n):
        _c = _a+_b
        _a = _b
        _b = _c
    return _c

print(fibo(int(input("Enter n:"))))
