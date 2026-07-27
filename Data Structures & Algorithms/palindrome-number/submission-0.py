class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        div = 1
        while x >= 10 * div:
            div *= 10
        
        while x:
            rightDigit = x % 10
            leftDigit = x // div
            if rightDigit != leftDigit:
                return False
            x = (x % div) // 10
            div = div // 100

        return True