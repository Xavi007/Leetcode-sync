class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        import itertools
        def helper(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        a, b = nums[i], nums[j]

                        rest = [nums[k] for k in range(len(nums)) if k != i and k != j]
                        for op in [a + b, a - b, b - a, a * b]:
                            if helper(rest + [op]):
                                return True
                        if b != 0 and helper(rest + [a / b]):
                            return True
                        if a != 0 and helper(rest + [b / a]):
                            return True
            return False

        return helper([float(x) for x in cards])    