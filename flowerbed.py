class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                count += 1
            if count >= n:
                return True
            i += 1
        return False

# Example usage:
solution = Solution()
flowerbed = [1,0,0,0,1]
n = 1
print(solution.canPlaceFlowers(flowerbed, n))  # Output: True
