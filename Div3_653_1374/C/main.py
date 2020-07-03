from collections import deque

def solve():
    n = int(input())
    S = list(input())
    stack = deque([])
    for ch in S:
        if ch == ')':
            if len(stack) == 0 or stack[-1] != '(':
                stack.append(ch)
            else:
                stack.pop()
        else:
            stack.append(ch)
    print(len(stack) // 2)

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        solve()
        t -= 1