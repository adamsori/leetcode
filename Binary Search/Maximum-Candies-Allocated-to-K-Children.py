class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        def check(x):
            return sum(c//x for c in candies) >= k  # k = 3  x = 4 True, x = 6 False, x = 5 True

        left, right = 1, max(candies)    # 1, 8
        while left <= right:             # 
            mid = left+(right-left)//2   # 1+(8-1)//2 = 4, 5+(8-5)//2 = 6, 5+(5-5)//2 = 5
            if not check(mid):           # if return of check == False
                right = mid-1
            else:                        # return of check == True
                left = mid+1 
        return right
            