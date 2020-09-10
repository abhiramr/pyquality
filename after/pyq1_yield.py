def fib(n):
    def fibseq(n):
        '''
        Iteratively return the first n Fibonacci numbers, starting from 0.
        '''
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b

    return sum(v for v in fibseq(n))

print(len(str(fib(20))))