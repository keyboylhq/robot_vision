# -*- coding: utf-8 -*-
"""
author: LHQ
by keyboy
"""

import serial

# 连接串口
serial = serial.Serial('COM6', 115200, timeout=2)  # 连接COM14,波特率位115200
if serial.isOpen():
    print('串口已打开')
else:
    print('串口未打开')

# 关闭串口
serial.close()

if serial.isOpen():
    print('串口未关闭')
else:
    print('串口已关闭')