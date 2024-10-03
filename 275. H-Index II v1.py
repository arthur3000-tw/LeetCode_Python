class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations) - 1
        papers = len(citations)
        k = 0
        while left <= right:
            mid = (left + right) // 2
            if citations[mid] >= papers - mid:
                right = mid - 1
                k = papers - mid
            elif citations[mid] < papers - mid:
                left = mid + 1
        return k
