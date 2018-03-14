N = int(input())
calling=[int(x) for x in input().split()]
ideal=[int(y) for y in input().split()]

count = 0;

while(len(calling)!=0):
    if(calling[0] != ideal[0]):
        item=int(calling.pop(0))
        calling.append(item)
        count = count + 1
    else:
        del calling[0]
        del ideal[0]
        count = count +1
print(count)
