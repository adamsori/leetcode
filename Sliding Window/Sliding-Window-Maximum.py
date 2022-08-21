class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        nums = [1,3,-1,-3, 5]
        k = 2
        indexQ = deque()
        valQ = deque()
        
        res = []
        
        for i, n in enumerate(nums):
            
            # valQ = ([]) and 1 > None
            while valQ and n > valQ[-1]: 
               
                valQ.pop()
                indexQ.pop()
                
            valQ.append(n) # ([1])
            indexQ.append(i) # ([0])
            
            while i - indexQ[0] + 1 > k: # 
                valQ.popleft()
                indexQ.popleft()
                
            if i + 1 >= k:
                res.append(valQ[0])
                
        return res