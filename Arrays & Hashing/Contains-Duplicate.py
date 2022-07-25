class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_values_list = set()
        for num in nums:
            if num in unique_values_list:
                return True
            unique_values_list.add(num)
        return False