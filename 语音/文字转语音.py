
# 没用
# import pyttsx3
# # 初始化， 必须要有奥
# engine = pyttsx3.init()
#
# engine.say('Sally sells seashells by the seashore.')
# engine.say('The quick brown fox jumped over the lazy dog.')
# # 注意，没有本句话是没有声音的
# engine.runAndWait()

#
#
import win32com.client
# text = """小明喜欢采用语音输入方式，他觉得这比用纸、笔，甚至键盘输入要好很多"""
text = """打开微信"""
speaker = win32com.client.Dispatch("SAPI.SpVoice")
# speaker.Speak("我是语音阿斯顿发射点发射点，小灵！")
speaker.Speak(text)


# import speech
#
# speech.say(text)