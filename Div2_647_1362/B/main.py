# https://codeforces.com/contest/1362/problem/B


def solve():
    n = int(input())
    S = set(map(int, input().split()))
    ans = -1
    
    for k in range(1, 1025):
        Srev = set([k ^ s for s in S])
        if Srev == S:
            ans = k
            break
    
    print(ans)


if __name__ == '__main__':
    T = int(input())
    while T > 0:
        T -= 1
        solve()