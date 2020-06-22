# https://codeforces.com/contest/1362/problem/C


# 5 => 3
# 0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111
#    +1   +2   +1   +3   +1   +2   +1   +3   +1   +2   +1   +3   +1   +2   +1   +4

def solve():
    n = int(input())
    ans = 0
    for i in range(n.bit_length() + 1):
        if n & (1 << i):
            ans += (1 << (i + 1)) - 1
    print(ans)


if __name__ == '__main__':
    T = int(input())
    while T > 0:
        T -= 1
        solve()