N = int(input())
bits = [int(x) for x in raw_input().split()]
No = input()
for i in range(No):
    low, high = int(input().split())
    low -= 1
    high -= 1
    result = bits[low]
    count = 0
    resultList = []
    for i in range(low + 1, high + 1):
        result ^= bits[i]
    resultList.append(result)

    for i in range(low, high + 1):
        if bits[i] == 0:
            count += 1
    resultList.append(count)

    print(*resultList, sep='')



bits = [1,0,0,0,1]
low = 3
high = 5
low -= 1
high -= 1
result = bits[low]
count = 0
resultList = []

for i in range(low+1,high+1):
  result ^= bits[i]
resultList.append(result)

for i in range(low,high+1):
  if bits[i] == 0:
      count += 1
resultList.append(count)
print(resultList)

