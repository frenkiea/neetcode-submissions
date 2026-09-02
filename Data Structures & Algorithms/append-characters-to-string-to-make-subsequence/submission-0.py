class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if t[0] not in s:
            return len(t)
        
        q = []
        i = 0
        for j in range(len(s)):

            if s[j] in t[i:]:
                if s[j] == t[i]:
                    q.append(i)
                    i += 1
        
        return len(t) - len(q)

            

        