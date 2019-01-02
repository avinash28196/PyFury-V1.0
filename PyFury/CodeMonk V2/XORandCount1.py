N=int(input())
for i in range(N):
    l = [int(x) for x in raw_input().split()]
    result = l[0] ^ l[1]
    binN = "{:032b}".format(result)
    strB = list(binN)
    print(strB.count('1'))
