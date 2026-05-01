class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            if (n - 1) not in numSet:
                lenght = 1
                while (n + lenght) in numSet:
                    lenght += 1
                longest = max(lenght, longest)
        return longest