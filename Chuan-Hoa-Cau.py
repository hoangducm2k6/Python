import sys

def normalize(line):
    line = line.strip()

    if not line:
        return ""

    # kiểm tra dấu câu cuối
    if line[-1] in '.!?':
        punct = line[-1]
        line = line[:-1]
    else:
        punct = '.'

    # chuẩn hóa chữ + khoảng trắng
    words = line.lower().split()
    line = ' '.join(words)

    # viết hoa chữ đầu
    line = line.capitalize()

    return line + punct


def solve():
    for line in sys.stdin:
        line = line.rstrip('\n')
        if line.strip() == "":
            continue
        print(normalize(line))


solve()