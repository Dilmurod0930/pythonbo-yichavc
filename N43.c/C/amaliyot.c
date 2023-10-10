
class Solution:
    def longestPalindrome(self, s: str) -> str:
        natija = ''
        for i in range(len(s)):
            natija = max(natija, kengaytirish(s,i,i), kengaytirish(s,i,i+1), key=len)
        return natija
            
def kengaytirish(s: str,i,j):
    while i>=0 and j<len(s) and s[i]==s[j]:
        i-=1
        j+=1
    return s[i+1:j]