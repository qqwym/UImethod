# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from skins import openBox
from time import sleep
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    c1 = openBox.OpenBox("86skins.com",17700705213,"000000")#86
    # c1 = openBox.OpenBox("66steam.cn",17700705213,"yywym123")#66
    c1.login()
    sleep(2)
    c1.openBox(1)
    c1.lucky(2)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
