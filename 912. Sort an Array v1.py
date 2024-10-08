class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(nums,l,r):
            if l < r:
                p = quick_sort_part(nums,l,r)
                quick_sort(nums,l,p-1)
                quick_sort(nums,p+1,r)

        def quick_sort_part(nums,l,r):
            i = l
            j = r - 1
            p = r
            while i < j:
                while i < r and nums[i] < nums[p]:
                    i += 1
                while j > l and nums[j] >= nums[p]:
                    j -= 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
            if nums[i] > nums[p]:    
                nums[i], nums[p] = nums[p], nums[i]
            return i

        quick_sort(nums,0,len(nums)-1)
        return nums
