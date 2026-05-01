class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            indx = target - n
            if indx in prevMap:
                return [prevMap[indx],i]
            prevMap[n] = i