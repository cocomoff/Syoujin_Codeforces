def solve():
    # shovel: 2 a + b
    # sword: a + 2 b
    # max num. of possible ones
    a, b = map(int, input().split())
    if a < b:
        a, b = b, a

    ans = min((a + b) // 3, b)
    print(ans)

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        solve()