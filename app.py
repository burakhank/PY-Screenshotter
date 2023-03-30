import pyautogui
import configparser
import datetime
import time


config = configparser.ConfigParser()
config.read('Settings.ini') 
pcName = config.get("Settings","pcName") 
sleepTime = config.get("Settings","sleepTime") 



while(True):
    print('Screenshot!')
    date_time = datetime.datetime.now()
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'ss\\' + pcName + ' time'  + str(date_time.hour) + '-' +str(date_time.minute) + ' screen.png')
    time.sleep(int(sleepTime))