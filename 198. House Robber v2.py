class Solution:
    def rob(self, nums: List[int]) -> int:
        nums_length = len(nums)
        ans = [0] * nums_length
        for i in range(0,nums_length):
            if i == 0:
                ans[0] = nums[0]
            elif i == 1:
                ans[1] = max(nums[0],nums[1])
            else:
                ans[i] = max(ans[i-1],nums[i]+ans[i-2])
        return ans[nums_length-1]
