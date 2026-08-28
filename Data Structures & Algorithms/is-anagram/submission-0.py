class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def count(st):
            d = {}
            a = sorted(st)
            b = list(dict.fromkeys(a))
            for i in range(len(b)):
                dem = 0
                for j in range(len(a)):
                    if b[i] == a[j]:
                        dem += 1
                d[b[i]] = dem

            return d
        return count(s) == count(t)
        