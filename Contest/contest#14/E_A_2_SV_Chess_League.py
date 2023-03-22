n,m=list(map(int,input().split()))
a = list(map(int,input().split()))

idx = [i for i in range(2**n)]
result = []
def recur(ic):
    n = len(ic)
    if n == 0:
        return
    if n == 1:
        result.append(ic[0])
        return
    winners = []
    win = []
    loser = []
    ball = []
    flag = True
    for i in range(0,n,2):
        if abs(a[ic[i]] - a[ic[i+1]]) > 400:
            if a[ic[i]] > a[ic[i+1]]:
                winners.append(ic[i])
                win.append(ic[i])
                loser.append(ic[i])
                ball.append(ic[i])
            else:
                win.append(ic[i+1])
                winners.append(ic[i+1])
                loser.append(ic[i+1])
                ball.append(ic[i+1])
        else:
            winners.append(ic[i])
            win.append(ic[i+1])
            if flag:
                loser.append(ic[i])
                ball.append(ic[i+1])
                flag = False
            else:
                loser.append(ic[i+1])
                ball.append(ic[i])
                flag = True
    recur(winners)
    recur(win)
    recur(loser)
    recur(ball)
recur(idx)
print(*sorted(map(lambda item: item + 1 ,list(set(result)))))