class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            index = target - n
            if index in prevMap:
                return[prevMap[index], i]
            prevMap[n] = i
               