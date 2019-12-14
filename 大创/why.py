import json
path='./ggd11.txt'
f=open(path,"r")
content=f.read()
f.close()
content=json.loads(content)
list1=[]
for j in range(0,len(content)):
    list1.append(content[j][4][2])
print(list1)
if 0 in list1:
    print(8888888888)
half_index=int(len(list1)/2)
while list1[half_index]==0:
    half_index+=1        #折半处理

for key_points in range(0,25):
    half_index=int(len(content)/2)#中间帧
    while content[half_index][key_points][2]==0:
        half_index+=1
    for j in range(0,half_index+1):
        if content[j][key_points][2]==0:
            if j==0:
                times=0
                while content[j+times][key_points][2]==0:
                    times+=1
                for k in range(0,times):
                    content[k][key_points][2]=content[times][key_points][2]
            else:
                if content[j][key_points][2]==0 and content[j+1][key_points][2]!=0:
                    content[j][key_points][2]=(content[j-1][key_points][2]+content[j+1][key_points][2])/2
                elif content[j][key_points][2]==0 and content[j+1][key_points][2]==0:
                    times=0
                    while content[j+times][key_points][2]==0:
                        times+=1
                    for k in range(0,times):
                        content[j+k][key_points][2]=content[j-1][key_points][2]+((content[j+times][key_points][2]-content[j-1][key_points][2])/(times+1))*(k+1)

    for j in range(len(content)-1,half_index,-1):
        if content[j][key_points][2]==0:
            if j==len(content)-1:
                times=0
                while content[j-times][key_points][2]==0:
                    times+=1
                for k in range(0,times):
                    content[len(content)-k-1][key_points][2]=content[len(content)-1-times][key_points][2]
            else:
                if content[j][key_points][2]==0 and content[j-1][key_points][2]!=0:
                    content[j][key_points][2]=(content[j-1][key_points][2]+content[j+1][key_points][2])/2
                elif content[j][key_points][2]==0 and content[j-1][key_points][2]==0:
                    times=0
                    while content[j-times][key_points][2]==0:
                        times+=1
                    for k in range(0,times):
                        content[j-k][key_points][2]=content[j+1][key_points][2]+((content[j-times][key_points][2]-content[j+1][key_points][2])/(times+1))*(k+1)
