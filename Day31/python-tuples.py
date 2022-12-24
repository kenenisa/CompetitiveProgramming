#only works with pypy... 10 min wasted trying to make it work with python
if __name__ == '__main__':
    n = int(input())
    t= tuple(map(int, input().split()))
    print(hash(t))
