def make_combination(input_list):
    def rec(n):
        nonlocal S_list
        nonlocal combinations_list
        if n == len(input_list):
            print(S_list)
            combinations_list.append(list(S_list))
            return

        # ①の分岐生成
        rec(n + 1)

        # ②の分岐生成
        S_list[n] = 1
        rec(n + 1)

        S_list[n] = 0

    combinations_list = []
    S_list = [0 for i in range(len(input_list))]
    rec(0)
    return combinations_list


input_list = [1, 5, 7]
combibations_list = make_combination(input_list)
print(combibations_list)
print(len(combibations_list))
