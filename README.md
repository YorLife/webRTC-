# webRTC-
利用webRTC对语音进行处理，实现VAD和降噪处理
使用方法
语音处理代码文档
环境：vs2015  python3
文件：
1.	wav2pcm.py  将wav文件转换成pcm格式
2.	pcm2wav.py  将pcm格式转换成wav格式
3.	audio_process项目 对pcm格式文件使用vad算法，确定有效语音端点
4.	WebRtcAudioTest项目 对pcm格式文件使用ns进行降噪
使用流程：
1.	运行wav2pcm.py文件对wav格式文件进行处理，将其转成pcm格式，其中第一个红色方框里填写源文件目录(这里的反斜杠需要变成斜杠)，第二个红色方框里填写输出目录(这里的反斜杠需要变成斜杠)。
![加载失败](https://github.com/xiyihong/webRTC-/raw/master/images/1.png)
2.	用vs打开audio_process项目里source文件夹下的audioprocess.sln文件，运行项目，在console里面根据提示输入源文件目录（这里的源文件目录需要选择上一步得到的pcm文件目录，不能是wav格式的）和输出目录，回车就能自动对文件进行vad算法处理，确定音频端点。
![加载失败](https://github.com/xiyihong/webRTC-/raw/master/images/2.png)
![加载失败](https://github.com/xiyihong/webRTC-/raw/master/images/3.png)
 
3.	用vs打开WebRtcAudioTest项目文件夹下的WebRtcAudioTest.sln文件，运行项目，在console里面根据提示输入源文件目录（这里的源文件目录需要选择上一步vad算法处理得到的pcm文件目录）和输出目录，回车就能自动对文件进行降噪处理。
![加载失败](https://github.com/xiyihong/webRTC-/raw/master/images/4.png)
![加载失败](https://github.com/xiyihong/webRTC-/raw/master/images/5.png)
 
4.	运行pcm2wav.py文件，将pcm格式文件转换成wav格式, 其中第一个红色方框里填写源文件目录(这里的反斜杠需要变成斜杠)，第二个红色方框里填写输出目录(这里的反斜杠需要变成斜杠)
 
![加载失败](https://github.com/xiyihong/webRTC-/raw/master/images/6.png)

