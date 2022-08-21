# SOLUTION USING ITERTOOLS.COMBINATIONS
# import itertools
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         for L in range(0, len(nums)+1):
#            for subset in itertools.combinations(nums, L):
#                res.append(subset)
#         return res
    
# SOLUTION USING DFS RECURSIVELY
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        
        # i is the index that tells which element we are current visiting
        def dfs(i):
            print(subset, subset.copy())
            if i >= len(nums):
                res.append(subset.copy())
                print(res)
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)
            print(res)
        dfs(0)
        return res