class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = {}
        for i in nums:
            ans[i] = nums.count(i)
        
        ans = dict(sorted(ans.items(), key=lambda item: item[1] , reverse=True))
     
        final_ans = []
        counter = 1   
        for key in ans.keys():
            if counter > k:
                break
            final_ans.append(key)
            counter = counter+1
        return final_ans