n = int(input())
def run():
    if n == 1:
        return 0
    events = []
    for _ in range(n):
        events.append(list(map(int,input().split())))
    
    def sort_key(item):
        return item[0]
    
    events.sort(key=lambda item: item[0])
    
    memory = events[0]
    count = 0

    for i in range(1,n):
        if memory[0] < events[i][0] and events[i][1] < memory[1]:
            count += 1
        else:
            memory = events[i]
    return count
print(run())
