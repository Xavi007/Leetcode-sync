class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        target_set = set(target)
        target_idx = 0

        for i in range(1, n+1):

            if target_idx >= len(target):
                break

            result.append("Push")

            if i not in target_set:
                result.append("Pop")
            else:
                target_idx += 1
        return result
