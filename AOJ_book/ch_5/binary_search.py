import random
import time


def binary_search(x, n_list):
    left = 0
    right = len(n_list) - 1
    while left < right:
        mid = round((left + right) / 2)
        if n_list[mid] == x:
            return mid
        elif n_list[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return False


S = [random.randint(1, 10000) for i in range(1000000)]
T = set([random.randint(1, 10000) for i in range(100)])


# 二分探索
count = 0
start1 = time.time()
for t in T:
    if binary_search(t, S):
        count += 1
print("elapsed_time:{0}".format(time.time() - start1))
print(count)
