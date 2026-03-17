class Solution:
    def findComplement(self, num: int) -> int:
        k = num^((1<<num.bit_length())-1)
        return k
        
