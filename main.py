import pyautogui
import pydirectinput
import time

#roblox can only see pydirectinput

textalert = 'Let the game maximized, running at foreground and play button visible at screen, use pyautogui fail-safe to stop script running and alt+f4 the \".py\" script. Only press OK when done the previous steps.'
pyautogui.alert(text=textalert, title='EGG MacroFarm', button='OK')

def farm():
    pydirectinput.press('1')
    pydirectinput.click()
    pydirectinput.press('2')
    pydirectinput.click()
    pydirectinput.press('3')
    pydirectinput.click()
    pydirectinput.press('4')
    pydirectinput.click()
    pydirectinput.press('5')
    pydirectinput.click()
    pydirectinput.press('6')
    pydirectinput.click()
    pydirectinput.press('7')
    pydirectinput.click()
    time.sleep(0.01)

while 1 == 1:
    try:
        playbutton = pyautogui.locateCenterOnScreen("play.png")
        pydirectinput.moveTo(playbutton.x-30,playbutton.y, 1)
        pydirectinput.moveTo(playbutton.x,playbutton.y, 1)
        time.sleep(1)
        pydirectinput.click()
        time.sleep(1)
    except:
        farm()
