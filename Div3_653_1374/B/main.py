# https://codeforces.com/contest/1374/problem/B

def factorization(n):
    dic = {}
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            dic[i] = cnt

    if temp!=1:
        dic[temp] = 1

    if len(dic) == 0:
        dic[n] = 1
    return dic

def solve():
    n = int(input())
    if n == 1:
        print(0)
        return

    # 素因数分解
    fact = factorization(n)

    # 2と3以外の素因数があってはダメ
    for key in fact:
        if key != 2 and key != 3:
            print(-1)
            return

    # 2の回数が3の回数を越していてはダメ (6で割って消せない)
    if 2 in fact and 3 in fact:
        if fact[2] > fact[3]:
            print(-1)
            return
        else:
            num = fact[2]
            num += (fact[3] - fact[2]) * 2
            print(num)
            return
    elif 2 in fact and 3 not in fact:
        print(-1)
        return
    elif 2 not in fact and 3 in fact:
        print(2 * fact[3])
        return


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        solve()
        t -= 1