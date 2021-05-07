import tkinter as tk
from tkinter import ttk, filedialog, Text, Canvas, Label, NW, OptionMenu, Toplevel, font
from tkinter import *
import os
import subprocess
import pyqrcode
from PIL import Image, ImageTk


# ____________________Functions Area_________________________
# generate the qrcode
def make_qr():
    qrcode = pyqrcode.create(textBoxOfData.get(1.0, END))
    name_file_to_save = filedialog.asksaveasfilename(
        filetypes=(
            ("", "*.svg"),
        )
    )
    qrcode.svg(name_file_to_save + ".svg", scale=5)
    os.startfile(name_file_to_save + ".svg")
# End


x = "0"


# Wifi Window
def wifi_window():
    # make the window and its properties
    window2 = Toplevel(window)
    window2.geometry("350x350")
    window2.title("QrCode Maker - Share Your Wifi Password")
    window2.resizable(False, False)
    # Canvas Element to grid the other Elements
    canvas2 = tk.Canvas(window2, width=350, height=350)
    canvas2.grid(columnspan=3, rowspan=3)

    lab1 = ttk.Label(window2, text="chose the network you want")
    lab1.grid(column=1, row=0)
    options = tk.StringVar(window2)
    options.set(profiles[1])
    options.trace("w", option_changed)
    listOfWifiSSIDs = tk.OptionMenu(window2, options, *profiles)
    listOfWifiSSIDs.grid(column=1, row=1)
    submit_button = ttk.Button(window2, text='Submit', command=print_answers)
    submit_button.grid(column=1, row=2)
    global x
    x = options.get()


def option_changed(*args):
    print("the user chose he value {}".format(x))


def print_answers():
    # print("Selected Option: {}".format(x))
    password = nameAndPass.get(x)
    print(x)
    print(password)
    wifi_qrcode = pyqrcode.create("WIFI:S:" + x + ";T:WPA;P:" + password + ";;")
    name_of_wifi_file = filedialog.asksaveasfilename(
        filetypes=(
            ("", "*.svg"),
        )
    )
    wifi_qrcode.svg(name_of_wifi_file + ".svg", scale=5)
    os.startfile(name_of_wifi_file + ".svg")


# ____________________End Of Functions Area_________________________


# Get the Wifi_Passwords_____________________________________________
nameAndPass = {}
wifiData = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in wifiData if "All User Profile" in i]
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    nameAndPass[i] = results[0]
# print()
# End_________________________________________________________________


# Make  Window
window = tk.Tk()
window.title("QrCode Maker")
window.resizable(False, False)
window.geometry("400x445")
# App Icon
appIcon = tk.PhotoImage(file="qr-code.png")
window.iconphoto(False, appIcon)
# Logo
logo = Image.open("qr-code.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_canvas = Canvas(window, width=100, height=100)
logo_canvas.grid(column=0, row=0, pady=10, sticky="E")
img = ImageTk.PhotoImage(Image.open("qr-code.png"))
logo_canvas.create_image(50, 50, image=img)
# NameOfLogo
nameOfLogo = Label(window, text="Qrcode Maker", font=("Comic Sans MS", 15, "bold"))
nameOfLogo.grid(column=0, row=1, columnspan=2, sticky="NESW")
# label1
label1 = Label(window, text="Enter Data", font=("Comic Sans MS", 16))
label1.grid(column=0, row=2, pady=15)
# special variable
data = tk.StringVar()
# Entry to get the data
textBoxOfData = Text(window, width=27, height=10)
textBoxOfData.grid(column=0, row=3, padx=10)
# button to perform the process
button1 = ttk.Button(window, text="Do the magic", command=make_qr, width=23)
button1.grid(column=1, row=3, sticky="NESW")
# button to open wifi sharing widow
button2 = ttk.Button(window, text="Share your Wifi Password", command=wifi_window, width=30)
button2.grid(column=0, row=4, columnspan=2, padx=10, pady=5, sticky="NESW")
# copyright label
label2 = Label(window, text="Copyright © 2021 Abdullah Sayed Sallam. All rights reserved", font=("Comic Sans MS", 8))
label2.grid(column=0, row=5, columnspan=2, sticky="NESW")
# to keep the window opened
window.mainloop()


