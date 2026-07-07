class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        length = len(A)
        output = [0] * length
        common_count = 0
        nums_seen = set()
 
        for i in range(length):
            if A[i] in nums_seen:
                common_count += 1
            else:
                nums_seen.add(A[i])

            if B[i] in nums_seen:
                common_count += 1
            else:
                nums_seen.add(B[i])

            output[i] = common_count
        
        return output