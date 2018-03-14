str = 'All-convoYs-9-be:Alert1.'
#st = 'Epp-gsrzsCw-3-fi:Epivx5.'

code = str.encode('ascii')
stack = []

for character in str:
    if (character == '-' or character == '.' or character == ':'):
        stack.append(character)
    else:
        for code in str.encode('ascii'):
            res = code+4
            char = chr(res)
            stack.append(char)

print(*stack, sep='')