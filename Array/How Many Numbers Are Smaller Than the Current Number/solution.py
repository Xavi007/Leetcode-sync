class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dic = {}
        ans = []

        extra_arr = sorted(nums)
        for i in range (len(nums)):
            if(extra_arr[i] in dic):
                continue
            else:
                dic[extra_arr[i]] = i


        for i in range (len(nums)):
            ans.append(dic[nums[i]])
        return ans

