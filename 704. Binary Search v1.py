class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while True:
            index = (left + right) // 2
            if target == nums[left]:
                return left
            elif target == nums[right]:
                return right
            elif target == nums[index]:
                return index
                
            if left == index or right == index:
                return -1
            elif target > nums[index]:
                left = index
            elif target < nums[index]:
                right = index
