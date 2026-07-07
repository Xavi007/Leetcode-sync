class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sum_check = []
        store = {}
        result = -1
        for i in nums:
            char = str(i)
            number = 0 
            for j in char:
                number+=int(j)
            sum_check.append(number)
        for i in range(len(nums)):
            if sum_check[i] in store:
                result = (store[sum_check[i]]+nums[i]) if (store[sum_check[i]]+nums[i])>result else result
                store[sum_check[i]] = nums[i] if store[sum_check[i]] <nums[i] else store[sum_check[i]] 
            else:
                store[sum_check[i]] = nums[i]

        return result