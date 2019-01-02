# example = {}
# example.setdefault('a', []).append('apple')
# example.setdefault('b', []).append('boots')
# example.setdefault('c', []).append('cat')
# example.setdefault('a', []).append('ant')
# example.setdefault('a', []).append('apple')
#
# print(example)



N = int(input())
for i in range(N):
    Len = int(input())
    l = [int(x) for x in raw_input().split()]
    result = []
    loopUp = {}

    for i in l:
        binN = "{:032b}".format(i)
        strB = list(binN)
        count = strB.count('1')
        loopUp.setdefault(count, []).append(i)

    specific_keys_from_a_range = list(loopUp.values())[0:]
    for i in specific_keys_from_a_range:
        for item in i:
            result.append(item)
    print (' '.join(map(str, result)))

