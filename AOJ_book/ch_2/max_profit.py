import time
import random


def return_max(n_list):
    start = time.time()
    # 想定される価格の最小値 - 最大値
    max_diff = 1 - 10 ** 9
    for i in range(len(n_list)):
        for j in range(1, len(n_list)):
            # 買い付け時のindexは売却時のindexよりも小さくなければならない
            if i >= j:
                continue
            diff = n_list[j] - n_list[i]
            if diff > max_diff:
                max_diff = diff

    print("elapsed_time:{0}".format(time.time() - start))
    return max_diff


def return_max2(n_list):
    start = time.time()
    min_n = n_list[0]
    # 想定される価格の最小値 - 最大値
    max_diff = 1 - 10 ** 9
    for i in range(1, len(n_list)):
        max_diff = max(max_diff, n_list[i] - min_n)
        # このmin_nの更新を先にしてしまうと、価格が減少し続ける場合に同じ地点同士で利益計算してしまうので必ずmax_diffの計算後に更新する
        min_n = min(min_n, n_list[i])

    print("elapsed_time:{0}".format(time.time() - start))

    return max_diff


#増えたり減ったりする場合
n_list = [random.randint(1,10**9) for i in range(10000)]
#増加し続ける場合
n_list = [random.randint(1,10**9) for i in range(10000)]
n_list.sort()
print(n_list)
#減少し続ける場合
n_list = [random.randint(1,10**9) for i in range(10000)]
n_list.sort(reverse=True)
print(n_list)

print("answer", return_max(n_list))
print("answer", return_max2(n_list))
