# https://codeforces.com/contest/1374/problem/B

def solve():
    n = int(input())
    ans = 0
    while n != 1:
        if n % 6 == 0:
            n //= 6
            ans += 1
        elif n % 3 == 0:
            n //= 3
            ans += 2
        else:
            ans = -1
            break
    print(ans)


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        solve()
        t -= 1