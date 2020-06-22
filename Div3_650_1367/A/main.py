def solve():
    s = input()
    ans = "".join(s[i] for i in range(0, len(s), 2))
    ans += s[-1]
    print(ans)


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        solve()