# https://codeforces.com/contest/1343/problem/A

def solve():
    n = int(input())
    x = 1

    # x = n / (2^k - 1)
    for k in range(2, 30):
        fact = pow(2, k) - 1
        if n % fact == 0:
            print(n // fact)
            return

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        solve()
        t -= 1