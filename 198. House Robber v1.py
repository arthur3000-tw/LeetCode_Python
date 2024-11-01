class Solution:
    def rob(self, nums: List[int]) -> int:
        nums_length = len(nums)
        if nums_length == 1:
            return nums[0]
        if nums_length == 2:
            return max(nums[0],nums[1])
        ans = [0] * nums_length
        ans[0] = nums[0]
        ans[1] = nums[1]
        for i in range(2, nums_length):
            ans[i] = max(ans[0:i-1]) + nums[i]
        return max(ans[nums_length-1],ans[nums_length-2])
