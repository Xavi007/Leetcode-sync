class Solution:
    def specialTriplets(self, xyz: List[int]) -> int:
        modd = 10**9 + 7
        total = 0

        seen = {}
        furture = {}

        for num in xyz:
            furture[num] = furture.get(num, 0) + 1

        for val in xyz:
            furture[val] -= 1
            target = val * 2

            if target in seen:
                a = seen[target]
                b = furture.get(target, 0)
                total = (total + (a * b) % modd) % modd

            seen[val] = seen.get(val, 0) + 1

        return total