
import matplotlib.pylab as plt
fpc1=open('test_files\\t3\\PC1.txt')
fpc2=open('test_files\\t3\\PC2.txt')
pc1=[]
pc2=[]
for line in fpc1.readlines():
    temp=[]
    line=line.replace('\n','')
    line=line.split('	')
    temp.append([float(line[0]),line[1],line[2],int(line[3]),int(line[4])])
    pc1.append(temp)

for line in fpc2.readlines():
    temp=[]
    line=line.replace('\n','')
    line=line.split('	')
    temp.append([float(line[0]),line[1],line[2],int(line[3]),int(line[4])])
    pc2.append(temp)


'''find_packet=pc2[0]
packet_index=0
for packet in pc1:
    if packet[0][1]==find_packet[0][1] and packet[0][2]==find_packet[0][2] and packet[0][3]==find_packet[0][3] and packet[0][4]==find_packet[0][4]:break
    packet_index+=1
print(packet_index)

#for i in range(packet_index,len(pc1)):
    #print(pc1[i][0])

pc1=[pc1[i][0] for i in range(packet_index,len(pc1))]
pc2=[pc2[i][0] for i in range(len(pc2))]

lenpack=min(len(pc1),len(pc2))
pc1=pc1[:lenpack-1]
pc2=pc2[:lenpack-1]

print(pc1)
print(pc2)

pc22=pc2[1][0]
pc12=pc1[1][0]
pc11=pc1[0][0]
pc21=pc2[0][0]

pc1222=pc22+((pc12-pc11)-(pc22-pc21))/2
print(pc1222)
time_delta=pc12-pc1222
print(time_delta)

pc1=[i[0]-time_delta for i in pc1]
pc2=[i[0] for i in pc2]
print(pc1)
print(pc2)
time=[]
for i in range(len(pc1)):
    temp=round(abs(pc1[i]-pc2[i]),6)*1000
    time.append(temp)
print(time)

plt.title('HTTP 80')
plt.ylabel('packet delivery time, ms')
plt.xlabel('packet number')
plt.plot(time)
plt.grid()
plt.show()'''