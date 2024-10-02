class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i in range(len(nums)):
            nums_map[nums[i]] = i

        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in nums_map:
                if nums_map[remain] == i:
                    continue
                return [i,nums_map[remain]]
                # Time: O(n)
                # Space: O(n)
