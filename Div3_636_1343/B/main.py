# https://codeforces.com/contest/1343/problem/B

def solve():
    n = int(input())
    if n % 4 != 0:
        print("NO")
    else:
        ev = list(range(2, n + 1, 2))
        od = list(range(1, n + 1, 2))
        od[-1] = sum(ev) - sum(od[:-1])
        ans = ev + od
        print("YES")
        print(*ans)

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        solve()
        t -= 1