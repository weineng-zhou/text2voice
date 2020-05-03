# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 17:35:59 2018

@author: weineng.zhou
"""

import os
from aip import AipSpeech
import pygame

try:
    os.mkdir("audio")
except FileExistsError:
    pass

#你的 APPID AK SK
APP_ID = '14371003'
API_KEY = '6ACWsLOg3b7OyGUKGfHZfbXa'
SECRET_KEY = 'nA6WP1d05qBoUYqxplNAV1inf8IHGwj9'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY) 


f = open('./doc/文字.txt', 'r', encoding='gbk')
sentenses = f.read().replace('\n','')
f.close()

result  = client.synthesis(sentenses, 'zh', 1,
                           {'vol': 5,  # 音量，取值0-15，默认为5中音量
                            'per': 4,  # 发音人选择, 0为女声，1为男声，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女
                            'spd': 5,  # 语速，取值0-9，默认为5中语速
                            'pit': 5   # 音调，取值0-9，默认为5中语调
                            } 
                          ) 

# 识别正确返回语音二进制 错误则返回dict
if not isinstance(result, dict):    
    with open('./audio/语音.mp3', 'wb') as f:  
        f.write(result)
f.close()

file='./audio/语音.mp3'
pygame.mixer.init()
track = pygame.mixer.music.load(file)
pygame.mixer.music.play()
# pygame.mixer.music.fadeout(1000) 
# pygame.mixer.music.stop()


