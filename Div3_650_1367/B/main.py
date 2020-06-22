# https://codeforces.com/contest/1367/problem/B

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    pos = []
    even_pos = 0
    odd_pos = 0
    even = 0
    odd = 0
    for i in range(n):
        if i % 2 != A[i] % 2:
            pos.append(i)
            if i % 2 == 0:
                even_pos += 1
            else:
                odd_pos += 1
            if A[i] % 2 == 0:
                even += 1
            else:
                odd += 1
    if len(pos) == 0:
        print(0)
    elif len(pos) == 1 or even != odd:
        print(-1)
    else:
        print(even)
    
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        solve()