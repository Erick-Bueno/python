from colorsys import rgb_to_hsv
from turtle import width
import pyautogui
while True:
    img = pyautogui.screenshot(region=(32,180,638,548,)) #pegando a area do jogo
    width,height = img.size
    for x in range(0,width,5):
        for y in range(0,height,5):
            r,g,b = img.getpixel((x,y))
            print(r,g,b)
            if r == 255 and g == 20 and b == 74:
                pyautogui.click(32+x,180+y)


#img.save('Tela.png')
#while True:
   # pyautogui.displayMousePosition() #pegar a cor do objeto ou item q deseja fazer o click


   




#rgb da cor = 255,20,74

