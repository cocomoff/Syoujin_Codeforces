# https://codeforces.com/contest/1367/problem/D

from collections import Counter


def solve():
    s = input()
    m = int(input())
    b = list(map(int, input().split()))
    ans = ['' for _ in range(m)]
    cv = [(k, v) for k, v in Counter(s).items()]
    cv.sort(key=lambda x: x[0], reverse=True)

    count = 0
    cvi = 0
    while count != m:
        zeros = [i for i, x in enumerate(b) if x == 0]
        lz = len(zeros)
        count += lz
        while cv[cvi][1] < lz:
            cvi += 1
        c = cv[cvi][0]

        for zero_index in zeros:
            ans[zero_index] = c
            b[zero_index] = -1  # 使わない
        cvi += 1
        for i in range(m):
            if b[i] < 0:
                continue
            for zero_index in zeros:  # 0になった部分の影響度
                b[i] -= abs(i - zero_index)
    return("".join(ans))
    

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        ans = solve()
        print(ans)