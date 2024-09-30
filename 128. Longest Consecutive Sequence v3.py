class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        length = 0

        for num in nums_set:
            if num - 1 in nums_set:
                continue
            next_num = num + 1
            count = 1
            while next_num in nums_set:
                count += 1
                next_num += 1
            if count > length:
                length = count

        return length
        # Time: O(n)
        # Space: O(n)