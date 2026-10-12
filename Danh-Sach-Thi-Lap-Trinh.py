class Student:
    def __init__(self, idx, name, team_code, team_name, school):
        self.code = f"C{idx:03d}"
        self.name = name.strip()
        self.team_name = team_name
        self.school = school

    def __lt__(self, other):
        return self.name < other.name


def solve():
    n = int(input())
    team_map = {}

    # đọc team
    for i in range(1, n + 1):
        team_name = input().strip()
        school = input().strip()
        code = f"Team{i:02d}"
        team_map[code] = (team_name, school)

    m = int(input())
    students = []

    # đọc thí sinh
    for i in range(1, m + 1):
        name = input().strip()
        team_code = input().strip()

        team_name, school = team_map[team_code]

        students.append(Student(i, name, team_code, team_name, school))

    # sort theo tên
    students.sort()

    # output
    for s in students:
        print(s.code, s.name, s.team_name, s.school)


solve()