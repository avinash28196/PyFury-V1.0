stack = [-1]
for i in range(int(input())):
    t=[int(x) for x in input().split()]
    if t[0] == 1:
        s=stack.pop()
        if s==-1:
            print('No Food')
            stack.append(-1)
        else:
            print(s)
    else:
        stack.append(t[1])