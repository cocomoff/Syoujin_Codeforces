# https://codeforces.com/contest/1371/problem/A

# 1: 1 => 1
# 2: 1, 2 => 1
# 3: 1, 2, 3 => 3, 3 => 2
# 4: 1, 2, 3, 4 => 2, 4, 4 => 2
# 5: 1, 2, 3, 4, 5 => 5, 5, 5 => 3
# 6: 1, 2, 3, 4, 5, 6 => 3, 6, 6, 6 => 3
# 7: 1, 2, 3, 4, 5, 6, 7 => 7, 7, 7, 7 => 4

def solve():
    n = int(input())
    print((n + 1) // 2)

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        solve()