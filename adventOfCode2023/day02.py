import os

cd = os.getcwd()
with open(os.path.join(cd, 'adventOfCode2023', 'day02.txt'), 'r') as file:
    count = 0
    nums = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
            'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}
    df = {"red":12,"green":13,"blue":14}
    for line in file:
        line = line.strip()
        g = line.split(":")
        i = int(g[0].split(" ")[1].strip())
        df = {"red":0,"green":0,"blue":0}
        for k in g[1].strip().split("; "):
            for j in k.strip().split(", "):
                f,s = j.split(" ")
                f = int(f)
                df[s] = max(df[s],f)
        count += (df['red'] * df['blue'] * df['green'])
    print(count)
