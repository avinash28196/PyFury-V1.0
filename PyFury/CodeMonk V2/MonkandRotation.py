N = int(input())
for index in range(0,N):
    testCase = [int(x) for x in input().split()]
    steps = testCase[1]
    stack = [int(x) for x in input().split()]

    for index in range(steps):
        item = int(stack.pop())
        stack.insert(0,item)

    print(*stack, sep=' ')
