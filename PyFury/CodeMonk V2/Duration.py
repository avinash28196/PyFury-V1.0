N = int(input())
for i in range(N):
    duration = [int(x) for x in raw_input().split()]
    totalHr = (duration[2] - (duration[0]))
    totalMin = (abs(duration[1]-60) + duration[3])
    if totalMin > 60:
        totalHr += 1
        totalMin = totalMin - 60
    print totalHr-1, totalMin

