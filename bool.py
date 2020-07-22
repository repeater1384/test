import pandas as pd
df = pd.read_excel('C:/test/test/공정표.xlsx').fillna('')

dic = {}
for i in range(1,5):#1,2,3,4
    temp = df[f'{i}번초'].tolist()
    if temp[-1] == '':temp.pop()
    dic[f'{i}번초'] = temp

print(dic)
def getNames(dic,when):
    a,b = dic[f'{when}번초'].pop(0),dic[f'{when}번초'].pop(0)
    dic[f'{(when)%4+1}번초'].append(a)
    dic[f'{(when)%4+1}번초'].append(b)
    return a,b

for when in range(1,5):
    print(getNames(dic,when))
print(dic)