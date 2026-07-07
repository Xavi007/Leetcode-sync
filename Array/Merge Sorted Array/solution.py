class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last_idx_n1 = m - 1
        last_idx_n2 = n - 1
        insert_idx = m + n -1

        while((last_idx_n1 >= 0) and (last_idx_n2 >= 0)):
            if(nums1[last_idx_n1] > nums2[last_idx_n2]):
                nums1[insert_idx] = nums1[last_idx_n1]
                insert_idx -= 1
                last_idx_n1 -= 1
            else:
                nums1[insert_idx] = nums2[last_idx_n2]
                insert_idx -= 1
                last_idx_n2 -= 1
                
        while(last_idx_n2 >= 0):
            nums1[insert_idx] = nums2[last_idx_n2]
            insert_idx -= 1
            last_idx_n2 -= 1
