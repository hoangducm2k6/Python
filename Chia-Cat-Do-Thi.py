def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())

        adj = [[] for _ in range(n + 1)]
        for _ in range(m):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)

        # đếm thành phần liên thông
        def count_components(skip):
            visited = [False] * (n + 1)
            cnt = 0

            for i in range(1, n + 1):
                if i == skip or visited[i]:
                    continue

                cnt += 1
                stack = [i]
                visited[i] = True

                while stack:
                    u = stack.pop()
                    for v in adj[u]:
                        if v != skip and not visited[v]:
                            visited[v] = True
                            stack.append(v)

            return cnt

        base = count_components(-1)

        best = base
        answer = 0

        for u in range(1, n + 1):
            comp = count_components(u)

            if comp > best:
                best = comp
                answer = u

        print(answer)


solve()