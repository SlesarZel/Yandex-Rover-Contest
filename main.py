import struct
import math





def ReadInputConditions():
    a=[]
    a=input().split(" ") #input N, MaxTips, CostC

    #length of world

    N = int(a[0])


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
    SumOfBots = int(N // 15) + 1
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

        while map[x][y] == "#":
            y = y + 1
            if y >= N:
                x = x + 1
                y = 0
        botNum = i
        Bots.extend([botNum, x, y, False]) #botNum, current X, current Y, busyFlag
        mapWithBots[x][y] = "o"

def ReadInputOrder():

    a=int(input())

    CountOfNewOrders = a
    global CountOfOrders
    CountOfOrders = CountOfOrders + CountOfNewOrders
    b=[]

    for i in range(CountOfNewOrders):
            b.extend([i+1+CountOfOrders,list(input().split(" "))]) #globalOrderNumber,input X Y start, X Y finish
                                                                #учто ещё что координаты стартуют от 1, а массив от 0
    global UndeliveredOrders
    UndeliveredOrders.extend(b)





def GetOrderOnBoard():
    return 0
    #Bots[BotNum].extend([[CountOfOrders[NumOfOrder]]])
    #Bots[BotNum][3]=True #busyFlag
    #CountOfOrders

    #flagOrderInTransit
    #flagBotIsBusy


def DeliverOrderFinished():
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


N=4
MaxTips=20
CostC=10
T=7
D=7
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
mapWithBots = map[:]
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

print("UndeliveredOrders: ",UndeliveredOrders)
