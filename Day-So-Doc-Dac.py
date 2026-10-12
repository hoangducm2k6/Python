import sys


def solve():
    try:
        line1 = sys.stdin.readline()
        if not line1: return
        t = int(line1.strip())
    except EOFError:
        return

    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        a = list(map(int, sys.stdin.readline().split()))


        last_pos = {}
        prev_idx = [-1] * n
        next_idx = [n] * n

        for i in range(n):
            if a[i] in last_pos:
                prev_idx[i] = last_pos[a[i]]
            last_pos[a[i]] = i

        last_pos.clear()
        for i in range(n - 1, -1, -1):
            if a[i] in last_pos:
                next_idx[i] = last_pos[a[i]]
            last_pos[a[i]] = i

        def is_unique(i, l, r):
            return prev_idx[i] < l and next_idx[i] > r

        def check(l, r):
            if l >= r:
                return True


            for i in range(0, (r - l) // 2 + 1):

                if is_unique(l + i, l, r):
                    return check(l, l + i - 1) and check(l + i + 1, r)

                if is_unique(r - i, l, r):
                    return check(l, r - i - 1) and check(r - i + 1, r)

            return False


        if check(0, n - 1):
            print("YES")
        else:
            print("NO")


solve()