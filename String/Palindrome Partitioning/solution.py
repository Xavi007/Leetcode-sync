class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]

    def getAllparts(self, s: str, partition: list, ans: list):
        if len(s) == 0:
            ans.append(partition[:])  
            return

        for i in range(len(s)):
            left_part = s[:i+1]

            if self.isPalindrome(left_part):
                partition.append(left_part)
                self.getAllparts(s[i+1:], partition, ans)
                partition.pop()

    def partition(self, s: str):
        ans = []
        partition = []
        self.getAllparts(s, partition, ans)
        return ans