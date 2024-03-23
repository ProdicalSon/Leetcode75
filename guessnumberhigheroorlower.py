class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        
        while left <= right:
            mid = left + (right - left) // 2
            result = guess(mid)
            
            if result == 0:
                return mid
            elif result == 1:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1  
def guess(num):
    pick = 6  
    if num == pick:
        return 0
    elif num < pick:
        return 1
    else:
        return -1
solution = Solution()
n = 10
print(solution.guessNumber(n))  
