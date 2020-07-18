# @profile
# def fibo(n):
#     a,b = 0,1
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else: 
#         return fibo(n-1)+fibo(n-2)

# print(fibo(int(input("Enter n:"))))


from functools import lru_cache

@lru_cache(maxsize=None)
@profile
def fib(n):
    if n < 2:  # base case
        return n
    return fib(n-1) + fib(n-2)

if __name__ == "__main__":
  print(fib(int(input("Enter n:"))))