# https://codeforces.com/contest/1335/problem/A

from string import ascii_lowercase

def solve():
    n, a, b = map(int, input().split())
    ans = None

    base = ''
    i = 0
    while len(base) < a:
        if i < b:
            base += ascii_lowercase[i]
            i += 1
        else:
            base += 'a'

    for i in range(a, n):
        base += base[i % a]
    print(base)

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        solve()
        t -= 1