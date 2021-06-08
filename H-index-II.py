# TC: O(N) since we are iterating over all the input list. 
# SC: O(1) since we are not using any extra space.

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        for i in range(len(citations)): 
            diff = len(citations) - i
            if citations[i] >= diff: 
                return diff
        
        return 0
