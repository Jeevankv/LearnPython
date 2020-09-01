
import pyautogui
from PIL import ImageGrab

import time


def hit(key):
    pyautogui.keyDown(key)
    return


def isCollide(data):
    # Draw the rectangle for birds
    for i in range(270, 320):
        for j in range(410, 580):
            if data[i, j] > 100:
                hit("down")
                return
    # Draw the rectangle for Cactus
    for i in range(270, 325):
        for j in range(595, 700):
            if data[i, j] > 100:
                hit("up")
                return
    return


if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    # hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)

        # from numpy import asarray
        # print(asarray(image))

"""        # Draw the rectangle for cactus
        for i in range(270, 325):
            for j in range(595, 700):
                data[i, j] = 255

        # Draw the rectangle for birds
        for i in range(270, 320):
            for j in range(410, 580):
                data[i, j] = 155

        image.show()
        break

"""


