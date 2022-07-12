import pyautogui
# from search_file import *
from one_C import *
import cv2


def open_rdp():
    pyautogui.screenshot('screen\\worksreen.png')
    ss = pyautogui.locateOnScreen('screen\\rdp.png', confidence=0.9)
    rdpopen = pyautogui.center(ss)
    pyautogui.click(rdpopen)


open_rdp()
# start_1v()
open_entera()
recognize_documents()
greate_docks()
# check_type_dock()
# check_files()

