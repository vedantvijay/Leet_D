class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:    
        
        value = abs(hour+(minutes/60)-(minutes/5))*30
        return min(value,360-value)


        