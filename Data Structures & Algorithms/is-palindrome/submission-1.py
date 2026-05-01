class Solution:
    def isPalindrome(self, s: str) -> bool:
        #leetcode: valid palindrome
        s = [i for i in s.lower() if i.isalnum()]
        return s==s[::-1]