import random
import time


def isloadable(p, k, w_list):
    if sum(w_list) <= p * k:
        return True
    else:
        return False


def binary_solver(k, w_list):
    start = time.time()
    left = 0
    right = 10000
    while left < right:
        mid = round((left + right) / 2)
        if isloadable(mid, k, w_list):
            right = mid
        else:
            left = mid + 1
        if right - left == 1:
            if isloadable(left, k, w_list):
                print("elapsed_time:{0}".format(time.time() - start))
                return left
            else:
                print("elapsed_time:{0}".format(time.time() - start))
                return right

    print("elapsed_time:{0}".format(time.time() - start))
    return right


def linear_solver(k, w_list):
    start = time.time()
    p = 0
    while not (isloadable(p, k, w_list)):
        p += 1
    print("elapsed_time:{0}".format(time.time() - start))
    return p


# w_list = [8, 1, 7, 3, 9]
w_list = [random.randint(1, 100) for i in range(1000)]
k = 10
print(binary_solver(k, w_list))
print(linear_solver(k, w_list))

