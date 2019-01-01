test = int(input())
for i in range(test):
  lista = [int(x) for x in input().split()]
  listb =  [int(y) for y in input().split()]
  result = 0 
  listand=0
  N=lista[1]
  for i in range(N-1):
    result = listb[i]&listb[i+1]   
    listand = result
  
  if (listand & lista[0]) == '0':
    print ('Yes')
  else:
    print('No')
