import struct
import math


"""class Rover():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.serialNumber = 0
        self.looking = UP
        self.busy = False
        self.loaded = False
        self.orderNum = 0

    def moveRover(self, x, y):
        self.x = x
        self.y = y

    def getCoords(self):
        return self.x, self.y"""""


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


Cargo
cargo

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
        сargo.holdby = self

    def putCargo(self):
        self.holding = None



def ReadInputConditions():
    a=[]
    a=input().split(" ") #input N, MaxTips, CostC

    #length of world

    N = int(a[0]) - 1

    #coordinates from 0


    MaxTips = int(a[1])


    CostC = int(a[2])

    a=[]

    #add map of world
    for i in range(N):
            a.extend([list(input().split(" "))]) #input map


    map = a

    a=[]
    a = input().split(" ") #input T, D

    T = int(a[0])

    D = int(a[1])

def CountBots():
    global SumOfBots
    SumOfBots = int(N // 3) + 1
    if SumOfBots > 100: #Count of bots 1..100
        SumOfBots = 100
    print("CountBots, N=",N," SumOfBots: ", SumOfBots)


def PlaceBots():
    print("PlaceBots")
    global Bots
    global mapWithBots
    Bots =[]

    for i in range(SumOfBots):
        if i == 1 - 1:
            x = N//2-1
            y = N//2-1
        if i == 2 - 1:
            x = N
            y = N
        if i == 3 - 1:
            x = 0
            y = 0
        if i == 4 - 1:
            x = N
            y = 0
        if i == 5 - 1:
            x = 0
            y = N

        else:
            x = N
            y = N

        print(N)

        while map[x][y] == "#":
            y = y + 1
            if y >= N:
                x = x + 1
                y = 0
        botNum = i
        Bots.extend([[botNum, x, y, False]]) #botNum, current X, current Y, busyFlag, X Y not from 1 but from 0 (sic!)
        mapWithBots[x][y] = "o"

def ReadInputOrder():

    a=int(input())

    CountOfNewOrders = a
    global CountOfOrders
    CountOfOrders = CountOfOrders + CountOfNewOrders
    b=[]

    for i in range(CountOfNewOrders):
            b.extend([i+CountOfOrders,list(input().split(" "))]) #globalOrderNumber,input X Y start, X Y finish
                                                                #учти ещё что координаты стартуют от 1, а массив от 0
    global UndeliveredOrders
    UndeliveredOrders.extend(b)


def StartDeliverIteration():
    OrdersToBotsAssign()
    for i in range(60):     #1min = 60 steps of each bot
        for BotNumber in range(SumOfBots):
            BotStep(BotNumber)

def OrdersToBotsAssign():
    #пока что тупо номер заказа равен номеру бота
    for i in range(SumOfBots):
        N = i
        NumOfOrder = i
        if Bots[i][3] == False : #не занят заказом
            Bots[N].extend(NumOfOrder) #в конце дописан номер заказа на борту
            Bots[i][3] = True  # In delivery: busy=True


def BotStep(BotNumber):
    print("BotNumber: ", BotNumber)

    CurrentCoordinates=[Bots[BotNumber][1], Bots[BotNumber][2]]
    X = CurrentCoordinates[0]
    Y = CurrentCoordinates[1]
    #UndeliveredOrders = [GlobalNumberOfOrder,X start, Y start, X finish, Y finish]
    #Bots[-1] = NumOfOrder  == GlobalNumberOfOrder
    XX = UndeliveredOrders[Bots[-1]][1] - 1 #X not from 1 but from 0 (sic!)
    YY = UndeliveredOrders[Bots[-1]][2] - 1 #Y not from 1 but from 0 (sic!)

    #ЭТО БУДЕТ РАБОТАТЬ ТОЛЬКО БЕЗ ПРЕПЯТСТВИЙ
    if X != XX :
        if X < XX:
            X = X + 1
            print("Bot ", i, "step ", "RIGHT")
        else:
            X = X - 1
            print("Bot ", i, "step ", "LEFT")

    else:
        if Y != YY:
            if Y < YY:
                Y = Y + 1
                print("Bot ", i, "step ", "UP")
            else:
                Y = Y - 1
                print("Bot ", i, "step ", "DOWN")

    if X == XX:
        if Y == YY:
            print("Bot ", i, "deliver order ", Bots[-1])
            DeliverOrderFinished(i)

    #if map[x][y] = "#" :

    CurrentCoordinates = [X, Y]
    Bots[i][1] = CurrentCoordinates[0]
    Bots[i][2] = CurrentCoordinates[1]


def GetOrderOnBoard(BotNum):
    return 0
    #Bots[BotNum].extend([[UndeliveredOrders[NumOfOrder]]])
    #Bots[BotNum][3]=True #busyFlag
    #CountOfOrders

    #flagOrderInTransit
    #flagBotIsBusy


def DeliverOrderFinished(i):
    Bots[BotNum].pop(4)  #delete [NewOrder] from [botNum, x, y, busyFlag, [NewOrder]]
    Bots[BotNum][3] = False  # busyFlag
    #flagOrderDelivered


global N
global MaxTips
global CostC
global map

global T
global D

SumOfBots = 0
global CountOfNewOrders
global UndeliveredOrders


N=4 - 1
MaxTips=20
CostC=10
T=3
D=2
map=[['.', '.', '.', '.'],
     ['.', '#', '#', '#'],
     ['.', '.', '.', '.'],
     ['.', '.', '.', '.']]


global CountOfOrders
CountOfOrders = 0

global UndeliveredOrders
UndeliveredOrders = []

global DeliveredOrders
DeliveredOrders = []

print("start")
#ReadInputConditions()
CountBots()

mapWithBots = [] #карта для размещения роверов (# - препятствие, o - робот, . - пустое пространство)
mapWithBots = map.copy()
#map.copy() для копирования списка, а не ссылания на него !!!почему-то это не работает!!!

PlaceBots()


print(N, MaxTips, CostC, T, D)
print("Map: ")
for i in range(len(map)):
    print(map[i])


print("Map with bots: ")
for i in range(len(mapWithBots)):
    print(mapWithBots[i])

print("Bots: ", Bots)

for i in range(T):
    ReadInputOrder()
    StartDeliverIteration()

print("UndeliveredOrders: ",UndeliveredOrders)
class Rover():
    __init__():
        self.x = 0
        self.y = 0
    def setCoords(self,x=0,y=0):
        self.x = x
        self.y = y
    def getCoords(self):
        return self.x,self.y
