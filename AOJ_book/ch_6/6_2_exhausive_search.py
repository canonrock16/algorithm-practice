def solve(i, target):
    global input_list
    if target == 0:
        return True
    if i >= len(input_list):
        return False
    res = solve(i + 1, target) or solve(i + 1, target - input_list[i])
    return res


target = 5
input_list = [1, 5, 7, 10, 21]
solve(0, target)

target = 4
input_list = [2, 4, 17, 8]
solve(0, target)

target = 25
input_list = [2, 4, 17, 8]
solve(0, target)
