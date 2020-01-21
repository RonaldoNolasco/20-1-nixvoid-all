f = open("codigos-final.txt","r")
f1 = f.readlines()
for x in f1:
    x=x[:-2]
    print(x)