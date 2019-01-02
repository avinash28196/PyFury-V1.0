while True:
    try:
        N = int(input())
        if(N == '0'):
            print(0)
        else:
            binN = "{:032b}".format(N)
            strB = list(binN)
            listB = list(reversed(strB))
            for index, i in enumerate(listB):
                if i == '1':
                    print (pow(2, index))
                    break;
    except EOFError:
        pass
# try:
#     while(True):
#         N = int(input())
#         binN = "{:032b}".format(N)
#         strB = list(binN)
#         listB = list(reversed(strB))
#         for index, i in enumerate(listB):
#             if i == '1':
#                 print (pow(2,index))
#                 break;
# except EOFError:
#     pass
