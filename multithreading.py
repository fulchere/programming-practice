# testing multithreading

from math import sqrt
import threading

nums = [
    [i for i in range(1000, 100000)],
    [i for i in range(1000, 100000)],
    [i for i in range(1000, 100000)],
    [i for i in range(1000, 100000)]
]


def pms(arr):
    for n in arr:
        is_prime(n)


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, round(sqrt(n)) + 1):
        if n % i == 0:
            return False
    print(True)
    return True


def t(bl):
    if bl:
        threads = []
        for i in range(4):
            threads.append(threading.Thread(target=pms, args=(nums[i],)))

        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
    else:
        for num in nums:
            pms(num)


t(False)
