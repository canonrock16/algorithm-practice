import random
import time


def bubble_sort(n_list):
    start = time.time()
    swap_count = 0
    # Pythonは参照渡しであるので、新規オブジェクトを作成しないと元のリストが変更されてしまう
    sorted_list = list(n_list)
    for i in range(len(sorted_list)):
        for j in reversed(range(i + 1, len(sorted_list))):
            if sorted_list[j][1] < sorted_list[j - 1][1]:
                swap_count += 1
                tmp = sorted_list[j]
                sorted_list[j] = sorted_list[j - 1]
                sorted_list[j - 1] = tmp

    print("swap_count", swap_count)
    print("elapsed_time:{0}".format(time.time() - start))
    return sorted_list


def selection_sort(n_list):
    start = time.time()
    swap_count = 0
    # Pythonは参照渡しであるので、新規オブジェクトを作成しないと元のリストが変更されてしまう
    sorted_list = list(n_list)

    for i in range(len(sorted_list)):
        min_j = i
        for j in range(i, len(sorted_list)):
            if sorted_list[j][1] < sorted_list[min_j][1]:
                min_j = j
        if i != min_j:
            swap_count += 1
            tmp = sorted_list[i]
            sorted_list[i] = sorted_list[min_j]
            sorted_list[min_j] = tmp
        # print(sorted_list)

    print("swap_count", swap_count)
    print("elapsed_time:{0}".format(time.time() - start))
    return sorted_list


def is_stable(in_list, out_list):
    start = time.time()
    for i in range(len(in_list)):
        for j in range(i + 1, len(in_list)):
            for a in range(len(in_list)):
                for b in range(a + 1, len(in_list)):
                    if (
                        # in_list内に数字部分が同じ値があって,
                        in_list[i][1] == in_list[j][1]
                        # in_list[i]の値とin_list[j]の値の順番がout_list内で逆転していたら
                        and in_list[i] == out_list[b]
                        and in_list[j] == out_list[a]
                    ):
                        # それは安定でないソートである
                        print("False!!")
                        print("i", i)
                        print("j", j)
                        print("a", a)
                        print("b", b)
                        print("in_list_i", in_list[i])
                        print("in_list_j", in_list[j])
                        print("out_list_b", out_list[b])
                        print("out_list_a", out_list[a])
                        print("-------------")
                        return False
    print("elapsed_time:{0}".format(time.time() - start))
    return True


def make_card_list():
    n_list = []
    for string in ["S", "H", "C", "D"]:
        for num in range(1, 10):
            n_list.append(string + str(num))
    random.shuffle(n_list)
    return n_list


n_list = ["H4", "C9", "S4", "D2", "C3"]
n_list = make_card_list()
# n_list.sort(reverse=True)
n_list.sort()

# バブルソートのチェック
orig_sort = bubble_sort(n_list)
print(n_list)
print(orig_sort)
is_stable(n_list, orig_sort)


# 選択ソートのチェック
orig_sort = selection_sort(n_list)
print(n_list)
print(orig_sort)
is_stable(n_list, orig_sort)


n_list = make_card_list()
orig_sort = selection_sort(n_list)
while is_stable(n_list, orig_sort):
    n_list = make_card_list()
    orig_sort = selection_sort(n_list)

