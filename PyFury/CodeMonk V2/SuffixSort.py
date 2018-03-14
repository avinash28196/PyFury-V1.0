t = [str(x) for x in input().split()]

newResult = []
str = t[0]
theOne = int(t[1])
list(str)

result = []
for character in str:
    result.append(character)

lengthOfString = len(result)




for index in range(0,lengthOfString):
    suffix = result[index:lengthOfString]
    newResult.append(suffix)
    newResult.sort()

print(*newResult[theOne-1], sep='')
