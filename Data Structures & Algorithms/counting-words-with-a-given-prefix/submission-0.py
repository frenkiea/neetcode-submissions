class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = [0] *  len(words) 
        k = len(pref)

        for i in range(len(words)):

            if len(words[i]) < len(pref):
                count[i] = 0

            else:
                if words[i][:k] == pref:
                    count[i] = 1
                else:
                    count[i] = 0

        return sum(count) 
            
        

        
                
        