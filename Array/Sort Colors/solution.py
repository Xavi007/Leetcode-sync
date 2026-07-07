class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        
        idx = 0
        for i in range(0, 3):
            freq = counter.get(i, 0)
            nums[idx : idx+freq] = [i] * freq
            idx += freq