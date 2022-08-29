#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#coding:utf-8
# Filename:hello_world.py
# 验证服务器，并且收到的所有消息都回复'Hello World!'
import werobot
robot = werobot.WeRoBot(token='your token')
# @robot.handler 处理所有消息
@robot.handler
def hello(message):
    return 'Hello World!'
# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()

