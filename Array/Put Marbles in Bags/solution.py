class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k==1: return 0
        splits = []

        for i,j in zip(weights,weights[1:]): splits.append(i+j)

        splits.sort()

        mn = weights[0] + weights[-1] + sum(splits[:k-1])
        mx = weights[0] + weights[-1] + sum(splits[1-k:])

        return mx-mn