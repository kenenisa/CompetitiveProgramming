N = int(input())
theList = []
for _ in range(N):
    cmd = input()
    cmdl = cmd.split()
    if "print" in cmd:
        print(theList)
    elif "insert" in cmd:
        theList.insert(int(cmdl[1]),int(cmdl[2]))
    elif "remove" in cmd:
        theList.remove(int(cmdl[1]))
    elif "append" in cmd:
        theList.append(int(cmdl[1]))
    elif "sort" in cmd:
        theList.sort()
    elif "pop" in cmd:
        theList.pop()
    elif "reverse" in cmd:
        theList.reverse()
        