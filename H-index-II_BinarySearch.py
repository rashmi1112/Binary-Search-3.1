# TC: O(log N) since everytime we reduce half of the search space for processing. 
# SC: O(1) as we do not use any extra space.

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        low = 0 
        high = n - 1
        
        while low <= high: 
            mid = (low + high) // 2
            if citations[mid] == n - mid:
                return n - mid
            elif citations[mid] < n - mid: 
                low = mid + 1
            else: 
                high = mid - 1
        
        return n - low
