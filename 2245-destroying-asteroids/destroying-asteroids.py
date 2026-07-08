class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        # Sort asteroids from smallest to largest
        asteroids.sort()
        
        for ast in asteroids:
            # If the planet is too small, it gets destroyed
            if mass < ast:
                return False
            # Otherwise, destroy it and absorb its mass
            mass += ast
            
        return True
