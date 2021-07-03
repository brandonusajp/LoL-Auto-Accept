import pyautogui
import sys
import cv2
from time import sleep
from PIL import Image
image = Image.open('accept.png')
global accepted
accepted  = False

def findimage(image):
    button_location = pyautogui.locateOnScreen(image, confidence=0.7)
    if button_location is not None:
        return button_location

def click(image):
    global accepted
    if findimage(image) is not None:
        pyautogui.click(findimage(image))
        accepted = True

def main():
    while accepted == False:
        print(accepted)
        sleep(2)
        try:
            print("looking for accept")
            click(image)
        except:
            print("can't find accept")
    print(accepted)
    sys.exit(0)

if __name__ =='__main__':
    main()