def combination_set(candidates, target):
    def backtrack(target, start, comb):
        if target < 0:
            return
        if target == 0:
            result.append(list(comb))
            return
        for i in range(start, len(candidates)):
            comb.append(candidates[i])
            backtrack(target - candidates[i], i, comb)
            comb.pop()

    result = []
    backtrack(target, 0, [])
    return result

candidates = [2, 3, 6, 7]
target = 7
print(combination_set(candidates, target))