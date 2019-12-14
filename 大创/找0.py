import json
name='ggd23.txt'
path='./'+ name
f=open(path,"r")
content=f.read()
f.close()
content=json.loads(content)
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
            elif frames_id==len(content)-1:#如果是最后一帧
                content[frames_id][key_points_id][2]=content[frames_id-1][key_points_id][2] 
        #如果是中间贞
            else:
                if content[frames_id+1][key_points_id][2] and content[frames_id-1][key_points_id][2] !=0:#前后不等于0
                    gitcontent[frames_id][key_points_id
                    ][2]=(content[frames_id+1][key_points_id][2]+content[frames_id-1][key_points_id][2])/2
                else:#后面等于0
                    times=1
                    while content[frames_id+1+times][key_points_id][2]==0:
                        print(frames_id+1+times)
                        times+=1
                        if frames_id+1+times == len(content):
                            times-=1
                            break
                    print('over',frames_id+1+times)
                    step=(content[frames_id+times][key_points_id][2]-content[frames_id-1][key_points_id][2])/times+1
                    for k in range(times):
                        content[frames_id+k][key_points_id][2]=content[frames_id-1][key_points_id][2]+(k+1)*step



content=json.dumps(content)
f=open(path,"w")
f.write(content)
f.close()
