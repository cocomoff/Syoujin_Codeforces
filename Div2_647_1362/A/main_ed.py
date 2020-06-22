def get_r(a):
    while a % 2 == 0:
        a //= 2
    return a

def solve():
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a

    r = get_r(a)
    if get_r(b) != r:
        print("-1")
        return

    count = 0
    b //= a
    while b >= 8:
        b //= 8
        count += 1
    if b > 1:
        count += 1
    print(count)

if __name__ == '__main__':
    T = int(input())
    while T > 0:
        T -= 1
        solve()