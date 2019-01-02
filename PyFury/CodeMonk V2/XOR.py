Test = int(input())
for i in range(Test):
    N = int(input())
    count = 0
    for i in range (1,N+1):
        for j in range(i+1, N+1):
            # print (i, j)
            xor = i ^ j
            if (xor <= N  or xor == N):
                count += 1
    print(count)



