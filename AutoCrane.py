import pyautogui
import PIL
import time

from PIL import Image


cheeseTextures = []



def findCursed(filename):
    needle = Image.open("Auto_Crane_Game/data/" + filename + ".png")
    rotatedImage = needle
    pyautogui.moveTo(326, 939)

    # searching for cursed cheese
    for i in range(36):
        pos = pyautogui.locateCenterOnScreen(rotatedImage, region = (290, 575, 1575 - 290, 800 - 575), confidence = 0.7)
        if pos == None:
            print(filename, i)
            rotatedImage = needle.rotate(i * 10)
        else:
            print(pos)
            break

    if(pos == None):
        return False

    # move mouse to cursed cheese
    pyautogui.moveTo(pos)

    #move mouse up to where claw is
    #pyautogui.moveTo(pos.x, 354)

    x = int(pos.x)

    # wait until claw moves left
    while pyautogui.pixelMatchesColor(1575 - 290, 354, (151, 113, 74)):
        pass

    #check if mouse color is no longer the brown color 37, 150, 190
    while pyautogui.pixelMatchesColor(x+5, 354, (151, 113, 74)):
        pass
    #click
    pyautogui.mouseDown(); pyautogui.mouseUp()
    return True

while True == True:
    if findCursed("gem") == False:
        if findCursed("needle") == False:
            if findCursed("cheese1") == False:
                print("FAILED")
                pyautogui.mouseDown(); pyautogui.mouseUp()
    while pyautogui.pixelMatchesColor(270, 290, (255, 241, 210)) == False:
        time.sleep(1)
        print("still playing")
    pyautogui.mouseDown(); pyautogui.mouseUp()






#for pos in pyautogui.locateAll("PyAutoGUI/curse.png", "PyAutoGUI/haystack.png", grayscale = False):
# print(w, x, y, z)