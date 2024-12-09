class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_alt = 0
        curr_alt = 0
        
        for alt in gain:
            curr_alt += alt
            
            highest_alt = max(highest_alt,curr_alt)
            
        return highest_alt