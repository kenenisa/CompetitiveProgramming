class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(key = lambda k: k[0])

        line = []
        for p,s in cars:
            line.append((target-p)/s) 

        fleet = 0
        while len(line) > 1:
            lead = line.pop()
            if lead < line[-1]:
                fleet += 1
            else:
                line[-1] = lead
        return (fleet + len(line))