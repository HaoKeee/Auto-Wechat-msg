#coding:utf-8
import sys
import time
import pyautogui
import pyperclip
import alchemy as db

class Wechat(object):
    def __init__(self):
        self.err_times = 3
    
    def get_input_position(self, png):
        print('请打开微信客户端')
        try_times = 0
        input = pyautogui.locateOnScreen(png)
        while not input:
            time.sleep(1)
            try_times += 1
            input = pyautogui.locateOnScreen(png)
            if try_times >= 120:
                print(f'check if opened wechat and search input like {png} to rebuild {png}')
                sys.exit()
        return input

    def search_group(self, box, text):
        try_times = 0
        print(box)
        print(pyautogui.center(box))
        while not pyautogui.locateOnScreen('./images/clicked-search.png'):
            pyautogui.leftClick(pyautogui.center(box))
            try_times += 1
            time.sleep(1)
            if try_times >= 5:
                print('check if correctly clicked search input bar to rebuild clicked-search.png')
                sys.exit()
        pyperclip.copy(text)
        time.sleep(0.2)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.press('enter')
        try_times = 0
        while not pyautogui.locateOnScreen('./images/check-searched.png'):
            pyautogui.leftClick(pyautogui.center(box))
            try_times += 1
            time.sleep(1)
            if try_times >= 5:
                print('check if correctly searched content to rebuild clicked-search.png or check-searched.png')
                sys.exit()
        return 

def main():
    wechat = Wechat()
    search_input = wechat.get_input_position('./images/search-input.png')
    wechat.search_group(search_input, '北京资产信息')
    group_input = wechat.get_input_position('./images/group-input.png')


if __name__ == '__main__':
    main()