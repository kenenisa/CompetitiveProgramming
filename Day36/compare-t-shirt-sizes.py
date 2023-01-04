
tests = int(input())
for _ in range(tests):
    left,right = input().split()
    l,r = len(left) ,len(right)
    result = '='
    if 'S' in left:
        if ('L' in right or 'M' in right) or l > r:
            result = "<" 
        elif l < r:
            result = ">" 
    elif 'L' in left:
        if ('S' in right or 'M' in right) or l > r:
            result = ">" 
        elif l < r:
            result = "<"
    elif 'M' in left:
        if 'L' in right:
            result = "<"
        elif 'S' in right:
            result = ">"
    print(result)
        