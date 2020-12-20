


fpc1=open('test_files/PC1.csv')
fpc2=open('test_files/PC2.csv')

pc1=[]
pc2=[]

for line in fpc1.readlines():
    line=line.replace('"','').split(',')
    pc1.append([float(line[0]),line[1],line[2],line[4]])

for line in fpc2.readlines():
    line=line.replace('"','').split(',')
    pc2.append([float(line[0]),line[1],line[2],line[4]])

for i in range(len(pc1)):
    print(print(pc1[i],pc2[i],end='\n'))



'''a=float(input('a'))
b=float(input('b'))
c=float(input('b'))
d=float(input('a'))

x1=abs(b-a)
x2=abs(c-d)
x3=(x1+x2)/2
b=b+x3
print('--',b-a)
c=c+x3
print('--',c-d)'''


