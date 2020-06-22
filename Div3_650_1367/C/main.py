# https://codeforces.com/contest/1367/problem/C

from bisect import bisect_left

def solve():
    N, K = map(int, input().split())
    # S = input()
    # S = [1] + list(map(int, list(input()))) + [1]
    S = list(map(int, list(input())))
    count = S.count(1)
    if count == 0:
        if K + 1 > N:
            return 1
        else:
            return N // (K + 1)

    ans = 0
    iS = [i for i in range(len(S)) if S[i] == 1]

    # 先頭
    if iS[0] > 0:
        ans += iS[0] // (2 * K)
    
    if iS[-1] < N - 1:
        ans += (N - 1 - iS[-1]) // (2 * K)

    for i in range(len(iS) - 1):
        if iS[i + 1] - iS[i] - 1  < 2 * K + 1:
            continue
        else:
            pos1 = iS[i + 1] - iS[i] - (2 * K + 1)
            num = pos1 // (K + 1)
            ans += (num + 1)
            # ans += (iS[i + 1] - iS[i] - K) // (2 * K)
            # print(iS[i], iS[i + 1])
    
    # # accum sum
    # SS = [0] * (N + 1)
    # for i in range(N):
    #     SS[i + 1] = S[i] + SS[i]
    # print(SS)

    # # count個 => この間に何個おけるかを計算する
    # for k in range(1, count):
    #     print(k)

    # i = 0
    # while i < N:
    #     if S[i] == '0':
    #         j = i + 1
    #         while j < min(N, i + K) and S[j] == '0':
    #             j += 1
    #         print(i, j)
    #         i = j
    #     else:
    #         i += 1
    return ans
    

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        ans = solve()
        print(ans)