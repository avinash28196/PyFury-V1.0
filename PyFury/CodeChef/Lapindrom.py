import math
N = int(input())

for index in range(0, N):
    lapin = str(input())
    strLen = len(lapin)
    mid = math.ceil(strLen / 2)
    LeftStr = []
    RightStr = []


    if mid%2!=0 :
        for i in range(0, mid-1):
            str(LeftStr.append(lapin[i]))
        for i in range (mid, strLen):
            str(RightStr.append(lapin[i]))

        sortL = sorted(LeftStr)
        sortR = sorted(RightStr)

        if(sortL == sortR):
            print("YES")
        else:
            print("NO")
    else:
        for i in range(0, mid):
            str(LeftStr.append(lapin[i]))
        for i in range(mid, strLen):
            str(RightStr.append(lapin[i]))

        if (LeftStr == RightStr):
            print("YES")
        else:
            print("NO")

