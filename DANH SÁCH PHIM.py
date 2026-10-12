n, m = map(int, input().split())

# đọc thể loại
genre = {}
for i in range(1, n + 1):
    genre["TL{:03d}".format(i)] = input()

class Film:
    def __init__(self, idx, ma_tl, ngay, ten, tap):
        self.ma = "P{:03d}".format(idx)
        self.theloai = genre[ma_tl]
        self.ngay = ngay
        self.ten = ten
        self.tap = tap

        d, m, y = map(int, ngay.split('/'))
        self.key_date = (y, m, d)

    def __str__(self):
        return f"{self.ma} {self.theloai} {self.ngay} {self.ten} {self.tap}"

films = []

for i in range(1, m + 1):
    ma_tl = input()
    ngay = input()
    ten = input()
    tap = int(input())

    films.append(Film(i, ma_tl, ngay, ten, tap))

films.sort(key=lambda x: (x.key_date, x.ten, -x.tap))

for x in films:
    print(x)