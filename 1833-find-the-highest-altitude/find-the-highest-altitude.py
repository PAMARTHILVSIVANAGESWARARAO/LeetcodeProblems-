class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0
        maxi = 0

        for g in gain:
            curr += g
            maxi = max(maxi, curr)

        return maxi