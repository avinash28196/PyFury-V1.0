string = raw_input()
string = string.lower()
vowelCount = 0
for index,i in enumerate(string):
    if i == 'a':
        vowelCount += (len(string) - index) * (index + 1)
    elif i == 'e':
        vowelCount += (len(string) - index) * (index + 1)
    elif i == 'i':
        vowelCount += (len(string) - index) * (index + 1)
    elif i == 'o':
        vowelCount += (len(string) - index) * (index + 1)
    elif i == 'u':
        vowelCount += (len(string) - index) * (index + 1)
print(vowelCount)

