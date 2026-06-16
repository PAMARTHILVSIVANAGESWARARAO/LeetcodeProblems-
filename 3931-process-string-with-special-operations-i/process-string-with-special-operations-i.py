class Solution:
    def processStr(self, s: str) -> str:
        res = []
        
        for char in s:
            if char.islower():
                res.append(char)
            elif char == '*':
                if res:
                    res.pop()
            elif char == '#':
                res = res + res
            elif char == '%':
                res.reverse()
                
        return "".join(res)