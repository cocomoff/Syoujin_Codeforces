# https://codeforces.com/contest/1374/problem/A

def solve():
    x, y, n = map(int, input().split())
    if n % x >= y:
        print(n - (n % x - y))
    else:
        # print(n - y - (y - n % x))
        print(n - (n % x - y) - x)
    
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        solve()
        t -= 1