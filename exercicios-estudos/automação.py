import pyautogui
import time
import keyboard
img = 'disc.PNG'
pyautogui.PAUSE = 0.5
pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('Enter')
time.sleep(1.5)
pyautogui.write('discord')
pyautogui.press('Enter')
time.sleep(3.0)
if pyautogui.locateOnScreen('disc.PNG'):
    pyautogui.moveTo(img)
    pyautogui.click()
time.sleep(5.0)
pyautogui.moveTo(75,130)
pyautogui.click()
pyautogui.moveTo(186,325)
pyautogui.click()
pyautogui.moveTo(453,686)
while True:
    pyautogui.write("penis")
    pyautogui.press("enter")

