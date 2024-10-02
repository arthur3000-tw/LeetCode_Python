class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        results = {}
        for num in nums:
            if num in results:
                results[num] += 1
            else:
                results[num] = 1
            if results[num] > len(nums)/2:
                return num
                # Time: O(n)
                # Space: O(n)
