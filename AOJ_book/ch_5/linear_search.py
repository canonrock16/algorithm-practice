import random
import time


def linear_search(x, n_list):
    for n in n_list:
        if x == n:
            return True
    return False


def linear_search_banpei(x, n_list):
    n_list.append(x)
    i = 0
    while x != n_list[i]:
        i += 1
    if i + 1 == len(n_list):
        n_list.pop(-1)
        return False
    n_list.pop(-1)
    return True


S = [random.randint(1, 10000) for i in range(1000000)]
T = set([random.randint(1, 10000) for i in range(100)])

# S = [2,5,6]
# T = [1,7]
# linear_search_banpei(1,S)
# print(S)

# 普通の線形探索
count = 0
start1 = time.time()
for t in T:
    if linear_search(t, S):
        count += 1
print("elapsed_time:{0}".format(time.time() - start1))
print(count)

# 番兵を用いた線形探索
count = 0
start2 = time.time()
for t in T:
    if linear_search_banpei(t, S):
        count += 1
print("elapsed_time:{0}".format(time.time() - start2))
print(count)

