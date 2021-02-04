import matplotlib.pylab as plt


test1=[]
test2=[]
test3=[]
test4=[]
test5=[]

def start(test_range):
    fpc1=open('test0202\\02022'+str(test_range)+'1.txt')
    fpc2=open('test0202\\02022'+str(test_range)+'2.txt')
    pc1=[]
    pc2=[]

    for line in fpc1.readlines():
        temp=[]
        line=line.replace('\n','').replace(' в†’','')
        while line[0]==' ':line=line[1:]
        line=line.split(' ')
        line.pop(0)
        s=''
        for i in range(3,len(line),1): s=s+str(line[i])
        line2=[[float(line[0]),line[1],line[2],s]]
        pc1.append(line2)
    print(pc1)

    for line in fpc2.readlines():
        temp=[]
        line=line.replace('\n','').replace(' в†’','')
        while line[0]==' ':line=line[1:]
        line=line.split(' ')
        line.pop(0)
        s=''
        for i in range(3,len(line),1): s=s+str(line[i])
        line2=[[float(line[0]),line[1],line[2],s]]
        pc2.append(line2)
    print(pc2)

    find_packet=pc2[0]
    packet_index=0
    for packet in pc1:
        if packet[0][1]==find_packet[0][1] and packet[0][2]==find_packet[0][2] and packet[0][3]==find_packet[0][3]:break
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
    return time


color=['','blue','red','orange','black','green']
for i in range(1,6):

    plt.title('Test '+str(i))
    plt.ylabel('packet delivery time, ms')
    plt.xlabel('packet number')
    plt.plot(start(i),color[i],label='Test_'+str(i))
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()
test1=start(1)
test2=start(2)
test3=start(3)
test4=start(4)
test5=start(5)

plt.title('Test 1..5')
plt.ylabel('packet delivery time, ms')
plt.xlabel('packet number')
plt.plot(test1,color = color[1], label='Test_1')
plt.plot(test2,color = color[2], label='Test_2')
plt.plot(test3,color = color[3], label='Test_3')
plt.plot(test4,color = color[4], label='Test_4')
plt.plot(test5,color = color[5], label='Test_5')
plt.legend(loc='upper left')
plt.grid()
plt.show()