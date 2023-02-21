import pyautogui
from tkinter import *
import time
import keyboard


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        my_font = ("times", 22, 'bold')
        my_font2 = ("times", 9)
        exitButton = Button(self, text="Exit", command=self.clickExitButton)
        clickButton = Button(self, text="Left click", command=self.clicktestButton)
        rightclickButton = Button(self, text="Right click", command=self.clickrightButton)
        nameauto = Label(text = "AutoClicker.exe", width=15, font=my_font)
        xcredits = Label(text = "Allah Is Great BBC gaming", font=my_font2)
        click_label = Label(text="Enter number of clicks:")
        click_label.pack(pady=10)
        self.click_entry = Entry()
        self.click_entry.pack(pady=10)

        xcredits.place(x=75,y=80)
        nameauto.place(x=-10,y=40)
        exitButton.place(x=250, y=490)
        clickButton.place(x=20, y=350)
        rightclickButton.place(x=20,y=400)

    # button functions
    def clickExitButton(self):
        exit()

    def clickrightButton(self):
        time.sleep(3)
        xy = 0
        while xy < int(self.click_entry.get()):
            pyautogui.rightClick()
            xy += 1

    def clicktestButton(self):
        time.sleep(3)
        y = 0
        while y < int(self.click_entry.get()):
            pyautogui.click()
            y += 1

    # auto-clicking function
    def auto_click(self):
        while keyboard.is_pressed('q'):
            pyautogui.click()

    # start auto-clicking when Q key is pressed
    def start_auto_click(self):
        if keyboard.is_pressed('q'):
            self.auto_click()
        else:
            self.master.after(10, self.start_auto_click)

    def run_auto_click(self):
        self.start_auto_click()

root = Tk()
app = Window(root)
root.wm_title("AutoClicker")
root.geometry("320x550")
app.run_auto_click() # start auto-clicking detection loop
root.mainloop()
