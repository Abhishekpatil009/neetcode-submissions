class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned=''
        sLowerCase=s.lower()
        for ch in sLowerCase:
            if ch.isalnum():
                cleaned+=ch
        
        reversedCleaned=cleaned[::-1]

        return reversedCleaned==cleaned



        