class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        results = {}
        for num in nums:
            if num in results:
                results[num] += 1
            else:
                results[num] = 1
            if results[num] > len(nums)/2:
                return num
