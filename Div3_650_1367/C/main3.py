# https://codeforces.com/contest/1367/problem/C


def solve():
    N, K = map(int, input().split())
    S = list(map(int, list(input())))
    b = []
    for i in range(N):
        if S[i] == 1:
            b.append(i)
    c = 0
    b.insert(0, -(K + 1))
    b.append(N + K)
    for i in range(1, len(b)):
        c += (b[i] - b[i - 1]) // (K + 1) - 1
    return c
    

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        ans = solve()
        print(ans)