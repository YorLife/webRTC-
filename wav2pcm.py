'''
wav格式 转换为 pcm格式
pcm 是没有头信息的，wav有44字节的头文件，所以去掉44字节的头文件
'''

import wave  
import numpy as np  
import os

#open a wave file, and return a Wave_read object  
#f = wave.open("C:/Users/xiyihong/Desktop/1.wav","rb")  
#read the wave's format infomation,and return a tuple  
#params = f.getparams()  
#get the info   
#nchannels, sampwidth, framerate, nframes = params[:4]  
#print("声道数%d 量化位数%d 采样速率%d 数据大小%d"%(nchannels,sampwidth,framerate,nframes))
# 采样速率是指每1秒钟采样的次数，因此每秒钟有16K的数据
#print("时间长度%f"%(nframes/framerate))
#Reads and returns nframes of audio, as a string of bytes.   
#str_data = f.readframes(nframes)  
##close the stream  
#f.close()  
#turn the wave's data to array  
#wave_data = np.fromstring(str_data, dtype = np.int16)  

#wave_data.tofile("C:/Users/xiyihong/Desktop/1.pcm")


g = os.walk(r"D:/code/final-voiceprint-test-b-20180630/voiceprint-test-b/data")  

for path,dir_list,file_list in g:  
    for file_name in file_list:  
        print(os.path.join(path, file_name) )
        f = wave.open(os.path.join(path, file_name),"rb")
        params = f.getparams()  
#get the info   
        nchannels, sampwidth, framerate, nframes = params[:4]  
        print("声道数%d 量化位数%d 采样速率%d 数据大小%d"%(nchannels,sampwidth,framerate,nframes))
# 采样速率是指每1秒钟采样的次数，因此每秒钟有16K的数据
        print("时间长度%f"%(nframes/framerate))
#Reads and returns nframes of audio, as a string of bytes.   
        str_data = f.readframes(nframes)  
#close the stream  
        f.close()  
#turn the wave's data to array  
        wave_data = np.fromstring(str_data, dtype = np.int16)  
        wave_data.tofile("D:/code/test-b/outlist/"+file_name.replace('wav','pcm'))