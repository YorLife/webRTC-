'''

pcm格式 转换为 wav格式
PCM格式文件 = 采样位数 + 采样位数 + 。。。
WAV格式文件所占容量（B) = （取样频率 X量化位数X 声道） X 时间 / 8 (字节= 8bit)
'''
import wave
import os
'''
# 读取pcm格式文件
f = open("D:/code/test-b/outlist/e0ebfb728b5caa811e5c43f292c73cad.pcm",'rb')
str_data  = f.read()

# 加入wav信息头，保存为wav格式
wave_out = wave.open("C:/Users/xiyihong/Desktop/1-out.wav",'wb')
wave_out.setframerate(16000)   #16KHZ（采样频率）
wave_out.setsampwidth(2)       #量化位数分为8位，16位，24位三种
wave_out.setnchannels(1)       #单声道振幅数据为n*1矩阵点，立体声为n*2矩阵点
wave_out.writeframes(str_data)
'''
g = os.walk(r"C:/Users/xiyihong/Desktop/test-b/list/list2")  
for path,dir_list,file_list in g:  
    for file_name in file_list:  
        print(os.path.join(path, file_name) )
        f = open(os.path.join(path, file_name),"rb")
        str_data  = f.read()
        wave_out = wave.open("C:/Users/xiyihong/Desktop/test-b/list/list2/"+file_name.replace('pcm','wav'),'wb')
        wave_out.setframerate(16000)   #16KHZ（采样频率）
        wave_out.setsampwidth(2)       #量化位数分为8位，16位，24位三种
        wave_out.setnchannels(1)       #单声道振幅数据为n*1矩阵点，立体声为n*2矩阵点
        wave_out.writeframes(str_data)