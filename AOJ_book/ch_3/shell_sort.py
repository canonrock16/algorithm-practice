import time
import random


def insertion_sort(n_list, g):
    # Pythonは参照渡しであるので、新規オブジェクトを作成しないと元のリストが変更されてしまう
    sorted_list = list(n_list)

    # リストのg番目からまず親ポインタを動かす
    for i in range(g, len(sorted_list)):
        # 今親ポインタがある要素を取得
        pointed_value = sorted_list[i]
        # 子ポインタ(親ポインタから左端に向かってg分離れた場所からg分ずつ左端に向かって動くポインタ)のインデックスを初期化
        j = i - g
        # 子ポインタのある場所の要素と親ポインタのある場所の要素を比較し、子ポインタのある場所の要素の方が大きかったら、親ポインタのある場所を子ポインタの要素で置き換える
        # 子ポインタのある場所の要素が親ポインタのある場所の要素よりも小さくなるか、小ポインタのインデックスが0を下回るまでループを回す。
        while j >= 0 and (sorted_list[j] > pointed_value):
            sorted_list[j + g] = sorted_list[j]
            # Pythonでは--のような演算子は使えない
            j -= g

        #最後に要素間の大きさの比較を行った子ポインタがある場所に親ポインタの要素を入れる
        sorted_list[j + g] = pointed_value

    return sorted_list


def shell_sort(n_list):
    start = time.time()
    g_list = []
    h = 1
    while h <= len(n_list):
        g_list.append(h)
        h = 3 * h + 1
    g_list.reverse()
    for g in g_list:
        sorted_list = insertion_sort(n_list, g)
    print("elapsed_time:{0}".format(time.time() - start))
    return sorted_list


# n_list = [3, 6, 1, 3, 6, 8, 5, 8]
# shell_sort(n_list)

n_list = [random.randint(1, 10 ** 9) for i in range(10000)]
# n_list.sort()
# n_list.sort(reverse=True)
orig_sort = shell_sort(n_list)
py_sort = sorted(n_list)
print(orig_sort == py_sort)

