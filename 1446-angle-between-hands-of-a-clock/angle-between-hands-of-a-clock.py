import math
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle = abs(30 * hour - 5.5 * minutes)
        
        # We need the smaller angle
        if angle > 180:
            return 360 - angle
        return angle