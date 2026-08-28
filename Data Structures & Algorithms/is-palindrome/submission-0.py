class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = ""
        for i in range(len(s)):
            t = ord(s[i])
            if (48 <= t and t <= 57) or (65 <= t and t <= 90) or    (97 <= t and t <= 122):
                p += s[i]

        p = p.lower()
        q = ""
        for j in reversed(range(len(p))):
            q += p[j]
        if p == q:
            return(True)
        else:
            return(False)
        