t = int(input())
for _ in range(t):
    def run():
        b = []
        for _ in range(3):
            b.append(list(input()))
        
        for i in range(3):
            row = set()
            col = set()
            for j in range(3):
                row.add(b[i][j])
                col.add(b[j][i])
            if len(row) == 1 and list(row)[0] != '.':
                return list(row)[0]
            if len(col) == 1 and list(col)[0] != '.':
                return list(col)[0]
        d1 = set([b[0][0],b[1][1],b[2][2]])
        if len(d1) == 1 and list(d1)[0] != '.':
            return list(d1)[0]
        d2 = set([b[0][2],b[1][1],b[2][0]])
        if len(d2) == 1 and list(d2)[0] != '.':
            return list(d2)[0]
        return "DRAW"
    print(run())