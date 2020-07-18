
with open('123.txt','w') as file:
    for i in range(32,128):
        file.write(chr(i)+'\n')