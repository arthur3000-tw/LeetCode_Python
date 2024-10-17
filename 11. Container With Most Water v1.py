class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_water = 0
        while l < r:
            tall = min(height[l],height[r])
            width = r - l
            current_water = tall * width
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

            max_water = max(current_water,max_water)
        return max_water
    # Time: O(n)
    # Space: O(1)
