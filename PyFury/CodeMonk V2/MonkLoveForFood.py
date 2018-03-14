N = int(input())
foodCost = []
for index in range(0,N):
    item = [int(x) for x in input().split()]
    if item[0]==2:
        foodCost.append(item[1])
    else:
        if not foodCost:
            print("No Food")
        else:
            print(foodCost[-1])
            del foodCost[-1]





