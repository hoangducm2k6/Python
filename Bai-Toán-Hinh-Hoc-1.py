def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def in_circle(a, b, c, p):
    ax, ay = a[0] - p[0], a[1] - p[1]
    bx, by = b[0] - p[0], b[1] - p[1]
    cx, cy = c[0] - p[0], c[1] - p[1]

    det = (
        (ax * ax + ay * ay) * (bx * cy - by * cx)
        - (bx * bx + by * by) * (ax * cy - ay * cx)
        + (cx * cx + cy * cy) * (ax * by - ay * bx)
    )

    return det


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        K = int(input())
        pts = [tuple(map(int, input().split())) for _ in range(n)]

        found = False

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if orient(pts[i], pts[j], pts[k]) == 0:
                        continue

                    sign = orient(pts[i], pts[j], pts[k])

                    cnt = 0
                    for p in pts:
                        val = in_circle(pts[i], pts[j], pts[k], p)

                        # điều chỉnh theo orientation
                        if sign > 0:
                            if val > 0:
                                cnt += 1
                        else:
                            if val < 0:
                                cnt += 1

                    if cnt == K:
                        print("YES")
                        found = True
                        break
                if found:
                    break
            if found:
                break

        if not found:
            print("NO")


solve()