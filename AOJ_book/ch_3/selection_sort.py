import random
import time


def selection_sort(n_list):
    start = time.time()
    swap_count = 0
    # Pythonは参照渡しであるので、新規オブジェクトを作成しないと元のリストが変更されてしまう
    sorted_list = list(n_list)

    for i in range(len(sorted_list)):
        min_j = i
        for j in range(i, len(sorted_list)):
            if sorted_list[j] < sorted_list[min_j]:
                min_j = j
        if i != min_j:
            swap_count += 1
        tmp = sorted_list[i]
        sorted_list[i] = sorted_list[min_j]
        sorted_list[min_j] = tmp

    print("swap_count", swap_count)
    print("elapsed_time:{0}".format(time.time() - start))
    return sorted_list


def selection_sort2(n_list):
    start = time.time()
    swap_count = 0
    # Pythonは参照渡しであるので、新規オブジェクトを作成しないと元のリストが変更されてしまう
    sorted_list = list(n_list)

    for i in range(len(sorted_list)):
        min_j = i
        for j in range(i, len(sorted_list)):
            if sorted_list[j] < sorted_list[min_j]:
                min_j = j
        if i != min_j:
            swap_count += 1
            # n_list[i]よりも小さい要素があった場合のみ交換処理を行う
            tmp = sorted_list[i]
            sorted_list[i] = sorted_list[min_j]
            sorted_list[min_j] = tmp

    print("swap_count", swap_count)
    print("elapsed_time:{0}".format(time.time() - start))
    return sorted_list


n_list = [2, 5, 7, 1, 7, 4, 8]
n_list = [random.randint(1, 10 ** 9) for i in range(10000)]
n_list.sort(reverse=True)
n_list.sort()
orig_sort = selection_sort2(n_list)
py_sort = sorted(n_list)
print(orig_sort)
print(n_list)
print(py_sort)
print(orig_sort == py_sort)

