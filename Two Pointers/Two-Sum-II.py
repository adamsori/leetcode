# The same solution for Two Sum problem in the Array Section works
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prevMap = {}
        
        for i, n in enumerate(numbers):
            result = target - n
            if result in prevMap:
                return [prevMap[result]+1,i+1]
            prevMap[n] = i
            

# Another solution
#class Solution:
#    def twoSum(self, numbers: List[int], target: int) -> List[int]:
#        l, r = 0, len(numbers) - 1
#        
#        while l < r:
#            curSum = numbers[l] + numbers[r]
#            
#            if curSum > target:
#                r -= 1
#            elif curSum < target:
#                l += 1
#            else:
#                return [l + 1, r + 1]
