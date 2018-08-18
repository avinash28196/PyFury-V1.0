


# X pages long poetry,Y pages left in it K rubles left for now,N Notbooks
# Pages,Cost
t = int(input())
for _ in range(t):
    x, y, k, n = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        d, e = map(int, input().split())
        a.append(d);
        b.append(e);

    for i in range(n):
        z = 0;
        if (x - y <= a[i] and k >= b[i]):
            z = 1;
            break;
        else:
            z = 0;

    if z:
        print("LuckyChef")
    else:
        print("UnluckyChef")