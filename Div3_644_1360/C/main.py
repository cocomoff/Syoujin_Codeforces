# https://codeforces.com/contest/1360/problem/C


def solve():
    n = int(input())
    A = list(map(int, input().split()))
    ne, no, eA, oA = 0, 0, [], []
    for a in A:
        if a % 2 == 0:
            eA.append(a)
            ne += 1
        else:
            oA.append(a)
            no += 1
    # groups = [0] * n
    # for i in range(n):
    #     for j in range(i + 1, n):
    #         if abs(A[j] - A[i]) < 1 or (A[j] % 2 == A[i] % 2):
    #             continue
    #         else:
    #             groups[j] = (1 - groups[i])

    if ne % 2 == 0 or no % 2 == 0:
        print("YES")
    else:
        # need to pair even and odd
        flag = False
        for a1 in eA:
            for a2 in oA:
                if abs(a1 - a2) <= 1:
                    flag = True
        if flag:
            print("YES")
        else:
            print("NO")
    
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        solve()