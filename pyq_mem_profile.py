from functools import lru_cache
import threading
import json
import sys
import time
import psutil
import os

def memory_instance():
    process = psutil.Process(os.getpid())
    info = process.memory_info()
    return info.rss / 1000000

def _get_memory():
    try:
        while True:
            print('Used memory {} M'.format(memory_instance()))
            time.sleep(2)
    except Exception as e:
        print('Exception in memory daemon - {}'.format(e))


def memory_profiler(func):
    def wrapper(*args):
        background_thread = threading.Thread(target=_get_memory, daemon=True)
        background_thread.start()
        func(*args)

    return wrapper


@lru_cache(maxsize=None)
# @profile
def fib(n):
    if n < 2:  # base case
        return n
    return fib(n-1) + fib(n-2)

@memory_profiler
def main():
    print(fib(int(input("Enter n:"))))

if __name__ == "__main__":
    main()