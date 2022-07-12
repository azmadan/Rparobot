import pyautogui

def open_rdp():
    pyautogui.screenshot('screen\\worksreen.png')
    ss = pyautogui.locateOnScreen('screen\\rdp.png', confidence=0.9)
    button7point = pyautogui.center(ss)
    pyautogui.click(button7point)


open_rdp()