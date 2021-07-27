import pyautogui
from config import global_config
from util import *
from wechat import wechat
from excel_screenshot import screenshot
from logger import logger

def main():
  root = global_config.getRaw('config','root')
  groups = get_all_groups(root)
  for group in groups:
    try:
      counts = read_xlsx_info(group['path'])
      text = get_text(group['location'],counts)
      screenshot._do_(group['path'])
      pyautogui.moveTo(3,3)
      wechat._do_(group['name'],group['path'],text)
      logger.info(f'{group["name"]} 完成')
    except Exception as e:
      logger.info(f'{group["name"]} 出现错误: {e}')

if __name__ == '__main__':
  main()