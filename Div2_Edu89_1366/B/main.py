# https://codeforces.com/contest/1366/problem/B 


def solve():
    n, x, m = map(int, input().split())
    al, ar = x, x
    for _ in range(m):
        li, ri = map(int, input().split())
        if li <= al and al <= ri:
            al = li
        if li <= ar and ar <= ri:
            ar = ri
    print(ar - al + 1)

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        solve()