class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        max_altitude = 0
        current_altitude = 0
        
        for altitude_gain in gain:
            current_altitude += altitude_gain
            max_altitude = max(max_altitude, current_altitude)
        
        return max_altitude

# Example usage:
solution = Solution()
gain = [-5,1,5,0,-7]
print(solution.largestAltitude(gain))  
