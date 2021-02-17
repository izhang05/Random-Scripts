import pyautogui
import time
import dvorak_to_qwerty


def sendMessageLoop(repeats, message):
    for _ in range(repeats):
        pyautogui.typewrite(message)
        pyautogui.press("enter")


def pasteLoop(repeats):
    for _ in range(repeats):
        pyautogui.hotkey("command", ".")
        pyautogui.press("enter")


def sepMessage(repeats, message):
    message = message.split()
    for _ in range(repeats):
        for i in message:
            pyautogui.typewrite(i)
            pyautogui.press("enter")


def sepChars(repeats, message):
    message = list(message)
    for _ in range(repeats):
        for i in message:
            pyautogui.typewrite(i)
            pyautogui.press("enter")


sendMessageLoop(1, "test")
# sendMessageLoop(1, dvorak_to_qwerty.convert("test"))
