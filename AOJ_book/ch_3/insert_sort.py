import time
import random


def insertion_sort(n_list):
    start = time.time()
    # Pythonは参照渡しであるので、新規オブジェクトを作成しないと元のリストが変更されてしまう
    sorted_list = list(n_list)

    # リストの1番目からまず親ポインタを動かす
    for i in range(1, len(sorted_list)):
        # 今親ポインタがある要素を取得
        pointed_value = sorted_list[i]
        # 子ポインタ(親ポインタがある場所から左端に向かって動いていくポインタ)のインデックスを親ポインタの左隣で初期化
        j = i - 1
        # 子ポインタのある場所の要素と親ポインタのある場所の要素を比較し、子ポインタのある場所の要素の方が大きかったら、子ポインタの右隣を子ポインタの要素に置き換える
        # 子ポインタのある場所の要素が親ポインタのある場所の要素よりも小さくなるか、小ポインタのインデックスが-1になるまでループを回す。
        while j >= 0 and (sorted_list[j] > pointed_value):
            sorted_list[j + 1] = sorted_list[j]
            # Pythonでは--のような演算子は使えない
            j -= 1
        # 子ポインタが停止した要素(親ポインタがある要素よりも小さい要素か、インデックスが-1の場所)の右隣に親ポインタがある要素を入れる
        sorted_list[j + 1] = pointed_value
    print("elapsed_time:{0}".format(time.time() - start))
    return sorted_list


n_list = [random.randint(1, 10 ** 9) for i in range(10000)]
n_list.sort()
orig_sort = insertion_sort(n_list)
py_sort = sorted(n_list)
print(orig_sort == py_sort)

