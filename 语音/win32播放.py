# -*- coding: utf-8 -*-
"""
author: LHQ
by keyboy
"""

# coding=utf-8
import win32api
# ShellExecute 查找与指定文件关联在一起的程序的文件名
# 第一个参数默认为0,打开，路径名，默认空，默认空，是否显示程序1or0
path ="D:\CCCCCCCCCCCCCCCCCCCCC\机器学习\语音\频谱\SimpleMusicVisualizer-master\SimpleMusicVisualizer-master\Miss Americana  The Heartbreak Prince.mp3"

win32api.ShellExecute(0, 'open', path, '', '', 1)