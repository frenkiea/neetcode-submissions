class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        dem = [0] * (len(blocks) - k + 1)
        for i in range(len(blocks) - k + 1):
            for j in range(i, i + k):
                if blocks[j] == 'W':
                    dem[i] += 1
        return min(dem)


            
             
        