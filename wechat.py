#coding:utf-8
import os
import sys
import time
import pyautogui
import pyperclip
from util import *

class Wechat(object):
    """
    微信操作
    """
    def __init__(self):
        pass
    
    def get_input_position(self, png):
        """
        获取输入框的位置
        png:输入框的截图地址(./images/?.png)
        """
        try_times = 0
        input = pyautogui.locateOnScreen(png)
        while not input:
            time.sleep(2)
            try_times += 1
            input = pyautogui.locateOnScreen(png)
            if try_times >= 120:
                print(f'检查是否打开微信且搜索栏同 {png} 决定是否重新截图 {png}')
                sys.exit()
        return input

    def search_group(self, box, text):
        """
        搜索群,切换到群
        box:pyautogui的Box对象
        text:群名
        """
        pyautogui.leftClick(pyautogui.center(box))
        pyperclip.copy(text)
        time.sleep(0.2)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(2)
        pyautogui.press('enter')
        return 
    
    def group_send(self):
        """
        对选定的群进行一次发送操作
        """
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        return 
    
    def _do_(self,group_name,file_path,text):
        """
        微信操作全部流程
        """
        print('请打开微信客户端')
        search_input = self.get_input_position('./images/search-input.png')
        self.search_group(search_input, group_name)
        copy_file(file_path)
        self.group_send()
        copy_file(f'{os.getcwd()}\screenshot.png')
        self.group_send()
        copy_text(text)
        self.group_send()
        return 

wechat = Wechat()
