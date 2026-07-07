class Solution:
    def largestGoodInteger(self, nums: str) -> str:
        if "999" in nums: return "999"
        if "888" in nums: return "888"
        if "777" in nums: return "777"
        if "666" in nums: return "666"
        if "555" in nums: return "555"
        if "444" in nums: return "444"
        if "333" in nums: return "333"
        if "222" in nums: return "222"
        if "111" in nums: return "111"
        if "000" in nums: return "000"
        return ""