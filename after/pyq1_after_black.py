'''
Finding the nth Fibonacci number
'''

def fibo(n):
    '''
    Returns the nth Fibonacci number
    '''
    a, b = 0, 1
    for i in range(1, n):
        c = a + b
        a = b
        b = c
    return c


print(fibo(int(input("Enter n:"))))
