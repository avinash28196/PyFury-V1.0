N = int(input())

def char_frequency(str1,str2):
    Value = 'NONE'
    dict1 = {}
    for n1 in str1:
        keys = dict1.keys()
        if n1 in keys:
            dict1[n1] += 1
        else:
            dict1[n1] = 1

    dict2 = {}
    for n2 in str2:
        keys = dict2.keys()
        if n2 in keys:
            dict2[n2] += 1
        else:
            dict2[n2] = 1

    if dict1 == dict2:
        Value = 'YES'
    else:
        Value='NO'
    return Value

for N in range(0,N):
    str1 = [str(x) for x in input().split()]
    res = char_frequency(str1[0],str1[1])
    print(res)


