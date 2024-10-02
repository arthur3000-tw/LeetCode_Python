class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            index = (left + right) // 2
            
            if target == nums[index]:
                return index
            elif target > nums[index]:
                left = index + 1
            elif target < nums[index]:
                right = index - 1
        return -1
        # Time: O(logn)
        # Space: O(1)
