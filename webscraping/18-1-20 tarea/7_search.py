f = open("codigos_sql.txt","r")
f1 = f.readlines()
for i in range (0,len(f1)):
    x=f1[i].split()
    num = x[0][:-1]
    if(int(num)>19950000 and int(num)<20200000):
        if(x[1]=='I1' or x[1]=='I2'):
            y=x[2].split('-')
            if(y[0]=='LOPEZ'):
                print(x)