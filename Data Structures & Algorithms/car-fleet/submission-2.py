class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed = list(zip(position, speed))
        posSpeed.sort(key = lambda x: x[0], reverse = True)
        stack = []
        for x in posSpeed:
            arrival = (target - x[0]) / x[1]
            if stack and stack[-1] >= arrival:
                continue
            else:
                stack.append(arrival)
                
        return len(stack)

        