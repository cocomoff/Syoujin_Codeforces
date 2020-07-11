# https://codeforces.com/contest/1360/problem/C


# def factorization(n):
#     arr = []
#     temp = n
#     for i in range(2, int(-(-n**0.5//1))+1):
#         if temp%i==0:
#             cnt=0
#             while temp%i==0:
#                 cnt+=1
#                 temp //= i
#             arr.append([i, cnt])

#     if temp!=1:
#         arr.append([temp, 1])

#     if arr==[]:
#         arr.append([n, 1])

#     return arr

def solve():
    n, k = map(int, input().split())
    # fn = factorization(n)

    lv = [1]
    v = 2
    while v * v <= n:
        if n % v == 0:
            lv.append(v)
            if n // v != v: lv.append(n // v)
        v += 1
    lv.append(n)
    lv.sort()
    ans = 1
    av = [n]
    for value in lv[1:]:
        if value <= k:
            av.append(n // value)
            ans = value
    print(n // ans)

    
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        solve()