import json
import os
file_dir=r'C:\Users\wsq\Desktop\First_try\all_points_without_z\data'
filelist=[]
for root,dirs,files in os.walk(file_dir):
    for file in files:
        if 'txt' in file:
            filelist.append(file)
print(filelist)            
for names in filelist:
    path= file_dir+"\\" + names
    f=open(path,'r')
    content=f.read()
    f.close()
    content=json.loads(content)
    for frame in range(0,len(content)):
        for key_points in range(0,25):
            del content[frame][key_points][2]
    content=json.dumps(content)
    f=open(path,"w")
    f.write(content)
    f.close()
'''
'''