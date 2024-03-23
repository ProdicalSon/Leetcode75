class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = max(candies)
        result = []
        for candy_count in candies:
            if candy_count + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        return result

# Example usage:
solution = Solution()
candies = [2,3,5,1,3]
extraCandies = 3
print(solution.kidsWithCandies(candies, extraCandies))  
