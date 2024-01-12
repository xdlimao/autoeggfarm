import pyautogui
import pydirectinput
import time

#roblox can only see pydirectinput


textalert = 'Let the game maximized, english language, running at foreground and play button visible at screen, use pyautogui fail-safe to stop script running and alt+f4 the \".py\" script. Only press OK when done the previous steps.'
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
    time.sleep(1)

while 1 == 1:
    try:
        playbutton = pyautogui.locateCenterOnScreen("play.png")
        pydirectinput.moveTo(playbutton.x-30,playbutton.y)
        pydirectinput.moveTo(playbutton.x,playbutton.y)
        time.sleep(1)
        pydirectinput.click()
        #for some reason, i need to use autogui to move mouse twice to avoid bugs from not real movement
        pyautogui.moveTo(playbutton.x,playbutton.y-301, 0.5)
        pydirectinput.moveTo(playbutton.x,playbutton.y-300)
        time.sleep(2)

    except:
        try:
            reconnectbutton = pyautogui.locateCenterOnScreen("ferr.png")
            pydirectinput.moveTo(reconnectbutton.x-30,reconnectbutton.y)
            pydirectinput.moveTo(reconnectbutton.x,reconnectbutton.y)
            time.sleep(1)
            pydirectinput.click()
            time.sleep(10)

        except:
            farm()
