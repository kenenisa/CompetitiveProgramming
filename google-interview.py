import decimal
import math
prime = []
LIMIT = 10**5
used = [False] * LIMIT
for i in range(2, LIMIT):
    if not used[i]:
        for j in range(i, LIMIT, i):
            used[j] = True
        prime.append(i)
print(len(prime))


def factorial(n):
    factorials = [1]
    for i in range(1, n + 1):
        factorials.append(factorials[i - 1] * i)
    return factorials


def compute_e(n):
    decimal.getcontext().prec = n + 1
    e = 2
    factorials = factorial(2 * n + 1)
    for i in range(1, n + 1):
        counter = 2 * i + 2
        denominator = factorials[2 * i + 1]
        e += decimal.Decimal(counter / denominator)
    return e


e = str(compute_e(10000)).replace(".", "")
# print(e)
n = len(e)
r = 0
w = []

for i in range(10):
    w.append(e[i])
    r += 1


def isPrime(num):
    for p in prime:
        if num % p == 0:
            return False
    return True


def run(r,n):
    while r < n:
        num = int("".join(w))
        if 7427466391 == num:
            return num
        w.pop(0)
        w.append(e[r])
        r += 1
    return "😔"
print(run(r,n))


# for i in range(2,int(math.sqrt(4590452011))+1):
#     if 4590452011 % i == 0:
#         print(i,"is a factor ----------")
# print("THE END?")
