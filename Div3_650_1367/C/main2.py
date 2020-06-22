# https://codeforces.com/contest/1367/problem/C

from math import ceil, floor

def solve():
    N, K = map(int, input().split())
    S = list(map(int, list(input())))
    count = S.count(1)
    if count == 0:
        if K > N:
            return 1
        else:
            return ceil(N / (K + 1))

    ans = 0
    iS = [i for i in range(len(S)) if S[i] == 1]

    # 先頭
    if iS[0] > 0:
        ans += iS[0] // (2 * K)
    
    if iS[-1] < N - 1:
        ans += (N - 1 - iS[-1]) // (2 * K)

    for i in range(len(iS) - 1):
        rem = iS[i + 1] - iS[i] - 1
        if rem < 2 * K + 1:
            continue
        else:
            pos1 = rem - (2 * K + 1)
            num = pos1 // (K + 1)
            ans += (num + 1)
    return ans
    

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        ans = solve()
        print(ans)