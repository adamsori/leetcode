class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            # m = l + ((r-l) // 2) 
            m = (l + r) // 2 # Em algumas linguagens essa operacao pode gerar um overflow, por conta do tamanho dos numeros. Nao precisamos nos preocupar com esse problema em Python. Mas para evitar esse problema em outra linguagem, basta usar o calculo da linha acima. 
            
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
            
        return -1
        