from math import log2, ceil, floorA

T = int(input())
while T > 0:
    T -= 1
    a, b = map(int, input().split())

    if a > b:
        a, b = b, a

    if a == b:
        print(0)
    elif b % a == 0:
        if (b // a) % 2 != 0:
            print(-1)
        else:
            # 8, 4, 2の順番でまるめていく
            fact = log2(b // a)
            if ceil(fact) != floor(fact):
                print(-1)
            else:
                num_f = ceil(log2(b // a))
                count = 0
                if num_f >= 3:
                    count += num_f // 3
                    num_f = num_f % 3
                if num_f >= 2:
                    count += num_f // 2
                    num_f = num_f % 2
                if num_f >= 1:
                    count += num_f
                    num_f = 0
                print(count)
    else:
        print(-1)
