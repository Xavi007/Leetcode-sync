class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        n = len(arr)


        direct_cost = sum(abs(arr[i] - brr[i]) for i in range(n))
    

        arr_counts = Counter(arr)
        brr_counts = Counter(brr)
    
        common_elements = 0
        for element, count in arr_counts.items():
            common_elements += min(count, brr_counts.get(element, 0))
    
        if common_elements == n: # if all elements are same after rearrangement no need to consider the cost of rearrangement
            return min(direct_cost, 0)
        else:
            rearrangement_cost = k
            remaining_arr = []
            remaining_brr = []
            for element, count in arr_counts.items():
                diff = count - brr_counts.get(element, 0)
                remaining_arr.extend([element] * max(0,diff))
            for element, count in brr_counts.items():
                diff = count - arr_counts.get(element, 0)
                remaining_brr.extend([element] * max(0,diff))
            
            remaining_cost = sum(abs(a - b) for a, b in zip(sorted(remaining_arr),sorted(remaining_brr)))
    
            return min(direct_cost, rearrangement_cost + remaining_cost)