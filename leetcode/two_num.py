# ブルートフォース例
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if (i != j) and (nums[i] + nums[j] == target):
                return [i, j]


# Hashmap例
def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i, num in enumerate(nums):
        search_key = target - num
        if search_key not in hashmap:
            hashmap[num] = i
        else:
            return [i, hashmap[search_key]]


# [3,3]target=6でダメになる例
def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i, num in enumerate(nums):
        hashmap[num] = i
        search_key = target - num
        if (search_key in hashmap) and (i != hashmap[search_key]):
            return [i, hashmap[search_key]]

