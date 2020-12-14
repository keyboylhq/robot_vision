# -*- coding: utf-8 -*-
"""
author: LHQ
by keyboy
"""
import threading
import win32com.client
import _thread
import pythoncom
# text = """小明喜欢采用语音输入方式，他觉得这比用纸、笔，甚至键盘输入要好很多"""
import time

# speaker.Speak("我是语音阿斯顿发射点发射点，小灵！")
for i in range(100000):
    time.sleep(0.5)
    if i<10000 and i>2:
        continue
    def g():
        pythoncom.CoInitialize()#加上的
        text = """打开微信"""
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        # speaker.Speak("我是语音阿斯顿发射点发射点，小灵！")
        speaker.Speak(text)
    add_vido=threading.Thread(target=g)
    add_vido.start()
    print(i)
    # _thread.start_new_thread ( g, args=text[0] )
