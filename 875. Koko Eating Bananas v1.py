class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while True:
            mid = (left + right) // 2
            hour = 0
            for pile in piles:
                hour += math.ceil(pile / mid)
            if hour <= h:
                if left == mid:
                    return mid
                right = mid
            else:
                left = mid + 1
        # Time: O(n * logn)
        # Space: O(1)
