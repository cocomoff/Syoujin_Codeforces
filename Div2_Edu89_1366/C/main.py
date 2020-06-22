# https://codeforces.com/contest/1366/problem/C
# https://codeforces.com/blog/entry/78735

def solve():
    # shovel: 2 a + b
    # sword: a + 2 b
    # max num. of possible ones
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    # 距離group (0, 1, ..., n + m - 2)
    counter = [[0, 0] for _ in range(n + m - 1)]
    for i in range(n):
        for j in range(m):
            counter[i + j][grid[i][j]] += 1

    ans = 0
    for p in range(n + m - 1):
        q = n + m - 2 - p
        if p >= q:
            continue

        # group (p, q) -> 0
        c1 = counter[p][0] + counter[q][0]
        # group (p, q) -> 1
        c2 = counter[p][1] + counter[q][1]
        ans += min(c1, c2)
    print(ans)

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        solve()