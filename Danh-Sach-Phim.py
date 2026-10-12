class Movie:
    def __init__(self, idx, genre, date, name, eps, genre_name):
        self.code = f"P{idx:03d}"
        self.genre = genre
        self.genre_name = genre_name
        self.date = date
        self.name = name
        self.eps = int(eps)

        d, m, y = map(int, date.split('/'))
        self.key = (y, m, d, name, -self.eps)

    def __lt__(self, other):
        return self.key < other.key


def solve():
    n, m = map(int, input().split())

    # đọc thể loại
    genre_map = {}
    for i in range(1, n + 1):
        name = input().strip()
        code = f"TL{i:03d}"
        genre_map[code] = name

    # đọc phim
    movies = []
    for i in range(1, m + 1):
        genre = input().strip()
        date = input().strip()
        name = input().strip()
        eps = input().strip()

        movies.append(Movie(i, genre, date, name, eps, genre_map[genre]))

    # sort
    movies.sort()

    # output
    for mv in movies:
        print(mv.code, mv.genre_name, mv.date, mv.name, mv.eps)


solve()