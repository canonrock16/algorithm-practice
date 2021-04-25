import random
import time


def bubble_sort(n_list):
    start = time.time()
    swap_count = 0
    # Pythonは参照渡しであるので、新規オブジェクトを作成しないと元のリストが変更される
    sorted_list = list(n_list)
    flg = 1
    while flg:
        flg = 0
        for i in reversed(range(1, len(sorted_list))):
            if sorted_list[i] < sorted_list[i - 1]:
                swap_count += 1
                tmp = sorted_list[i]
                sorted_list[i] = sorted_list[i - 1]
                sorted_list[i-1] = tmp
                flg = 1

    print("swap_count", swap_count)
    print("elapsed_time:{0}".format(time.time() - start))
    return sorted_list


n_list = [random.randint(1, 10 ** 9) for i in range(10000)]
n_list.sort(reverse=True)
n_list.sort()
orig_sort = bubble_sort(n_list)
py_sort = sorted(n_list)
print(orig_sort == py_sort)

