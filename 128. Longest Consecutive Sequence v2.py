class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        length = 0

        for num in nums:
            count = 0
            if num - 1 in nums_set:
                continue
            next_num = num
            while next_num in nums_set:
                count += 1
                next_num += 1
            if count > length:
                length = count

        return length
