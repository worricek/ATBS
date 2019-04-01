import pyautogui

print('Press Ctrl-C to quit.')
try:
    while True:
    # Get and print the mouse coordinates.
        pyautogui.moveRel(5, 0)
        pyautogui.moveRel(0, 5)
        pyautogui.moveRel(-5, 0)
        pyautogui.moveRel(0, -5)
        pyautogui.PAUSE = 9
except KeyboardInterrupt:
    print('\nDone.')
