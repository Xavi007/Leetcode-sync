class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        nums1_dict = {num1[0]: num1 for num1 in nums1}

        for num2 in nums2:
            key, value = num2[0], num2[1]
            
            if key in nums1_dict:
                nums1_dict[key][1] += value
            else:
                nums1_dict[key] = [key, value]

        nums1 = list(nums1_dict.values())
        nums1 = sorted(nums1_dict.values(), key=lambda x: x[0])

        return nums1

