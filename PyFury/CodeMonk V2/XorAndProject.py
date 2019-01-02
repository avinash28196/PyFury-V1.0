Test = int(input())
for test in range(Test):
    N = int(input())
    count = 0
    for D in range(1, N + 1):
        binN = "{:08b}".format(D)
        divisorList = list(binN)
        divisorCount = divisorList.count('1')

        result = N/D

        result = "{:08b}".format(result)
        resultList = list(str(result))
        resultCount = resultList.count('1')


        if resultCount <= divisorCount:
            count += 1

    print(count)


