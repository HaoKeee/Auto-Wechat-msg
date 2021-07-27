import os
import sys
import json
import time
import subprocess
import pyautogui
from config import global_config
from PIL import ImageGrab

class Screenshot(object):
  """
  对excel实现住宅表的截图+保存操作
  """
  def __init__(self):
    pass
  
  def open_xlsx(self, path):
    """
    打开excel
    path:路径
    """
    excel_path = global_config.get('config', 'excel_path')
    if not os.path.exists(excel_path):
      print('excel.exe路径错误')
      sys.exit()
    (filepath,tempfilename) = os.path.split(excel_path)
    current_path = os.getcwd()
    os.chdir(filepath)
    subprocess.Popen(f'{tempfilename} {path}')
    os.chdir(current_path)
    return 

  def switch_house(self):
    """
    切换表到住宅表
    """
    try_times = 0
    house_sheet = pyautogui.locateOnScreen('./images/house.png')
    while not house_sheet:
      if pyautogui.locateOnScreen('./images/house_opened.png'):
        return 
      house_sheet = pyautogui.locateOnScreen('./images/house.png')
      try_times += 1
      time.sleep(1)
      if try_times >= 60:
        print('未成功打开excel')
        sys.exit()
    pyautogui.click(pyautogui.center(house_sheet))
    time.sleep(1)
  
  def save_screenshot(self):
    """
    保存截图到./screenshot.png
    """
    coordinates = global_config.getRaw('config','screenshot_coordinates')
    coordinates = tuple(json.loads(coordinates))
    png_save_path = './screenshot.png'
    im = ImageGrab.grab(coordinates)
    if os.path.exists(png_save_path):
      os.remove(png_save_path)
    im.save(png_save_path)
  
  def close_xlsx(self):
    """
    关闭excel
    """
    pyautogui.hotkey('ctrl','f4')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(1)
    os.system('taskkill /F /im EXCEL.EXE')
    # if pyautogui.locateOnScreen('./images/close-failed.png'):
    #   return self.close_xlsx()
  
  def _do_(self, path):
    """
    excel截图全部流程
    """
    self.open_xlsx(path)
    self.switch_house()
    self.save_screenshot()
    self.close_xlsx()

screenshot = Screenshot()
