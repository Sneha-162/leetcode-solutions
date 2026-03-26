class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = sum(int(d) for d in str(x))
        return -1 if x%s else s

            
