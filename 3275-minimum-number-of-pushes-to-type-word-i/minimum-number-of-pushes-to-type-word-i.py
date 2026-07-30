class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        blk = n//8

        return (blk * (blk+1) * 4) +  (n % 8) * (blk + 1)