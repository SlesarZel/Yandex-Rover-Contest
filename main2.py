import pprint


class Path():
    def __init__(self, length=0, rover=None, toBase=False, path=[], toCargo=None):
        self.lenght = length
        self.rover = rover
        self.toBase = toBase
        self.path = path
        self.toCargo = toCargo
        # path = [[0,1],[0,2],[1,2],[2,2]]


class Cargo():
    def __init__(self, x=0, y=0, holdby=None, id=None, base=None):
        self.x = x
        self.y = y
        self.holdby = holdby
        self.id = id
        self.base = base


class Base():
    def __init__(self, x=0, y=0, id=None):
        self.x = x
        self.y = y
        self.id = id


class Rover():
    def __init__(self, x=0, y=0, holding=None):
        self.x = x
        self.y = y
        self.holding = holding

    def move(self, x, y):
        if abs(self.x - x) + abs(self.y - y) < 2:
            if abs(self.x - x) < 2 and abs(self.y - y) < 2:
                self.x = x
                self.y = y
            else:
                print("can't move rover at", self.x, ' ', self.y)

    def getCargo(self, cargo):
        self.holding = cargo
        cargo.holdby = self

    def putCargo(self):
        self.holding = None


labirint = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
labirintC = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
labirintR = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
labirintB = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Координаты входа [2,0], координаты выхода [8,0]. В которой 1 - это стена, 0 - это путь,
# Преубразую "стены" в пробелы для удобства
labirint111 = labirint
for y in range(0, len(labirint111)):
    for x in range(0, len(labirint111[y])):
        if labirint111[y][x] == 1:
            labirint111[y][x] = '#'
        if labirint111[y][x] == 0:
            labirint111[y][x] = ' '
y = 5
x = 5
labirint111[y][x] = 1  # присваиваю начальное значение ячейки входа


def wave(mapa, rover=None, forCargo=True, forBase=False)
    for yy in range(0, len(labirint111) - 1):
        for xx in range(0, len(labirint111[yy]) - 1):  # без еще одного внешнего цикла не доходит до конца

            for y in range(0, len(labirint111) - 1):
                for x in range(0, len(labirint111[y]) - 1):
                    if labirint111[y][x] != '#':

                        # left
                        if labirint111[y - 1][x] != '#' and labirint111[y - 1][x] == ' ' and labirint111[y][x] != ' ':
                            labirint111[y - 1][x] = int(labirint111[y][x]) + 1
                            if labirintC[y - 1][x] == 1 and forCargo:
                                path = createPath(mapa, y - 1, x, rover)
                        # forward
                    if labirint111[y][x + 1] != '#' and labirint111[y][x + 1] == ' ' and labirint111[y][x] != ' ':
                        labirint111[y][x + 1] = int(labirint111[y][x]) + 1
                    # right
                    if labirint111[y + 1][x] != '#' and labirint111[y + 1][x] == ' ' and labirint111[y][x] != ' ':
                        labirint111[y + 1][x] = int(labirint111[y][x]) + 1
                    # back
                    if labirint111[y][x - 1] != '#' and labirint111[y][x - 1] == ' ' and labirint111[y][x] != ' ':
                        labirint111[y][x - 1] = int(labirint111[y][x]) + 1

# pprint.pprint(labirint111)