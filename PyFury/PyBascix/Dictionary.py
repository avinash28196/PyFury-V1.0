users = [
        {'id':1010,'name':"Administrator",'type':1},
         {'id':1011,'name':"Administrator2",'type':1}
         ]

new_dict={}

for di in users:
    new_dict[di['id']]={}
    for k in di.keys():
        if k =='id': continue
        new_dict[di['id']][k]=di[k]

print (new_dict)