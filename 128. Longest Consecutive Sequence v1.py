class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = {}
        length = 0

        for num in nums:
            nums_dict[num] = False

        for num in nums:
            count = 1
            if nums_dict[num]:
                continue
            nums_dict[num] = True

            next_num = num + 1
            while next_num in nums_dict:
                nums_dict[num+1] = True
                count += 1
                next_num += 1
            
            next_num = num - 1
            while next_num in nums_dict:
                nums_dict[num-1] = True
                count += 1
                next_num -= 1
            
            if count > length:
                length = count
        
        return length
        # Time: O(n^2)
