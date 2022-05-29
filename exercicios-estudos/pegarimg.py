import pyautogui
#pyautogui.PAUSE = 2
#mg = pyautogui.locateOnScreen('disc.PNG')
#pyautogui.moveTo(img)
img = 'disc.PNG'
if pyautogui.locateOnScreen('disc.PNG'):
    pyautogui.moveTo(img)
    pyautogui.click()