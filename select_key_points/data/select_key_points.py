import json
import os
file_dir=r'C:\Users\wsq\Desktop\First_try\select_key_points\data'
filelist=[]
for root,dirs,files in os.walk(file_dir):
    for file in files:
        if 'txt' in file:
            filelist.append(file)

for names in filelist:
    path= file_dir+"\\" + names
    f=open(path,'r')
    content=f.read()
    f.close()
    content=json.loads(content)
    print(content)
    not_neccessary_point_id=[17,18,8,19,20,21,22,23,24]
    for frame in range(0,len(content)):
        times=0
        for j in not_neccessary_point_id:
            del content[frame][j-times]
            times+=1
        print(len(content[frame]))
    content=json.dumps(content)
    f=open(path,"w")
    f.write(content)
    f.close()
