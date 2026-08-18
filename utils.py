import pyautogui
import time
import random

def click(x, y):
    pyautogui.click(x, y)


def double_click(x, y):
    pyautogui.doubleClick(x, y)


def right_click(x, y):
    pyautogui.rightClick(x, y)


def move_and_click(x, y, delay=0):
    pyautogui.moveTo(x, y)
    time.sleep(delay)
    click(x, y)


def random_click(x_range, y_range, duration_range=(0, 1), delay=0):
    x = random.randint(*x_range)
    y = random.randint(*y_range)
    duration = random.uniform(*duration_range)
    pyautogui.moveTo(x, y, duration)
    time.sleep(delay)
    click(x, y)


def wait(seconds):
    time.sleep(seconds)
