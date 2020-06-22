# https://codeforces.com/contest/1335/problem/A

def solve():
    n = int(input())
    ans = None
    if n <= 2:
        ans = 0
    elif n % 2 != 0:
        ans = n // 2
    else:
        ans = n // 2 - 1
    print(ans)


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        solve()
        t -= 1