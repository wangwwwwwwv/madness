from scipy.fftpack import fft,ifft
import matplotlib.pyplot as plt
import json
import numpy as np
import math
import os
def get_feature(data):
    def find_z_is_0(content):
        for frames_id in range(len(content)):
            each_frame=content[frames_id]
            for key_points_id in range(len(each_frame)):
                key_points=each_frame[key_points_id]
                if key_points[2]==0:#如果z是0
                    if frames_id==0 and content[frames_id+1][key_points_id][2]==0:#如果是第一贞而且下一贞也是0
                        times=1
                        while content[frames_id+1+times][key_points_id][2]==0:#找出不是0的那一贞
                            times+=1
                        for k in range(times):
                            content[frames_id+k][key_points_id][2]=content[frames_id+1+times][key_points_id][2]
                    elif frames_id==0 and content[frames_id+1][key_points_id][2]!=0:#如果下一贞不是0
                        content[frames_id][key_points_id][2]=content[frames_id+1][key_points_id][2] 
                    if frames_id==len(content)-1:#如果是最后一帧
                        content[frames_id][key_points_id][2]=content[frames_id-1][key_points_id][2] 
                #如果是中间贞
                    else:
                        if content[frames_id+1][key_points_id][2] and content[frames_id-1][key_points_id][2] !=0:#前后不等于0
                            content[frames_id][key_points_id][2]=(content[frames_id+1][key_points_id][2]+content[frames_id-1][key_points_id][2])/2
                        else:#后面等于0
                            times=1
                            while content[frames_id+1+times][key_points_id][2]==0:
                                times+=1
                            step=(content[frames_id+1+times][key_points_id][2]-content[frames_id-1][key_points_id][2])/times+1
                            for k in range(times):
                                content[frames_id+k][key_points_id][2]=content[frames_id-1][key_points_id][2]+(k+1)*step
        return content
    
    data=json.loads(data)
    a=find_z_is_0(data)
    def fuliyebianhuan(a):
        #for key_points_number in range(0,25):
        z=[]
        xx=[j for j in range(len(a))]
        for j in range(len(a)):
            z.append(a[j][4][2])
        np.set_printoptions(threshold=np.inf) # 加上这一句


        plt.subplot(221)
        plt.plot(xx,z)
        plt.title('Original wave')

        zz=fft(z)                     #快速傅里叶变换
        test_z=zz
        for i in range(len(fft(z))):
            if  i >= 30:
                test_z[i] = 0
        test = np.fft.ifft(test_z)# 对变换后的结果应用ifft函数，应该可以近似地还原初始信号。
        z=test
        z1=np.real(z)
        z2=list(z1)
        plt.plot(xx,z,'r')
        plt.title('New wave)',fontsize=10,color='#F08080')
        plt.show()
        return z2
    #-----------------------计算算相邻两帧关节点位置坐标变化量矩阵-------------------------#
    #z2=fuliyebianhuan(a)#傅里叶变换滤波否？？？
    delta_distance_all=[]#所有
    for j in range(len(a)-1):
        delta_distance_keypoints_all=[]#每一帧所有关键点的xyz
        for keypoints in range(0,25):
            delta0=a[j+1][keypoints][0]-a[j][keypoints][0]
            delta1=a[j+1][keypoints][1]-a[j][keypoints][1]
            delta2=a[j+1][keypoints][2]-a[j][keypoints][2]#用不用傅里叶变换？？？
            delta_distance_keypoints_all.append([delta0,delta1,delta2])
        delta_distance_all.append(delta_distance_keypoints_all)
    #print(len(delta_distance_all))#【帧1，帧2，帧3......帧......】帧1：【关键点0，关键点1，关键点.....】【x,y,z】
    D_all=[]#【每帧D】【第几个关节点】【数】
    for each_frame in delta_distance_all:#each_frame:每帧的【关键点0，关键点1.。。。。】【x,y,z】
        each_frames=[]
        for keypoints in each_frame:
            summ=math.sqrt((keypoints[0]*keypoints[0])+(keypoints[1]*keypoints[1])+(keypoints[2]*keypoints[2]))#每帧每个关键点的距离矩阵
            each_frames.append(summ)
        D_all.append(each_frames)
    cutt=int(len(D_all)/4)+1#59
    D_4=[]
    D_all_np=np.array(D_all)
    #---------------------------------------------------------开始分四堆----------------------------------------------------
    for j in range(0,3):#分4堆
        addd=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],dtype=float)
        for k in range(cutt*j,cutt*(j+1)):
            addd+=D_all_np[k]
        D_4.append(addd)
    addd=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],dtype=float)
    for j in range(k+1,len(D_all_np)):
        addd+=D_all_np[j]
    D_4.append(addd)
    D_4=np.array(D_4)
    #print(D_4)
    return D_4
    #---------------------------------------------------------分四堆结束---------------------------------------------


f=open(r"C:\Users\wsq\Desktop\First_try\all_key_points\data\ggd11.txt","r")
data=f.read()
f.close()
d1=get_feature(data)

file_dir=r'C:\Users\wsq\Desktop\First_try\all_key_points\data'
filelist=[]
for root,dirs,files in os.walk(file_dir):
    for file in files:
        if 'txt' in file:     
            filelist.append(file)
print(filelist)
result_list=[]
for name in filelist:
    path=file_dir+'./'+name
    f=open(path,"r")
    content=f.read()
    f.close()
    each=get_feature(content)
    d3=int(np.linalg.norm(d1-each))
    result_list.append(d3)
print(result_list)



    

