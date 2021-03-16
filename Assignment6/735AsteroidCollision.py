class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0
        length = len(asteroids)
        
        while i < length:
            if len(stack) == 0:
                stack.append(asteroids[i])
        
            elif asteroids[i] > 0:
                stack.append(asteroids[i])
            
            elif asteroids[i] < 0 and stack[-1] < 0:
                stack.append(asteroids[i])
            
            elif asteroids[i] < -stack[-1]:
                stack.pop()
                i -= 1
                
            elif asteroids[i] == -stack[-1]:
                stack.pop()
                     
            i += 1
        return stack