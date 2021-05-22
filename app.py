import tkinter as tk
from tkinter import ttk, filedialog, END, Toplevel, Label, Text, PhotoImage, Frame
import ttkbootstrap
import subprocess
import pyqrcode
import os

# -------------------------------------------Functions Area----------------------------------------------

# Global Vars
window2 = ""
wifi_selected = ""
submit_button = ""
is_hidden = ""

# calc the center to center the widows 
def postion(window_name, wdith, height):
    # Gets half the screen width/height 
    positionRight = int((window_name.winfo_screenwidth() - wdith) /2)
    positionDown = int((window_name.winfo_screenheight() - height) /2)
    return positionRight, positionDown
# -----------End_func_1----------------

# Generate the qrcode
def make_qr():
    data_to_convert = str(textBoxOfData.get(1.0, END))
    if bool(data_to_convert.strip()):
        button1.configure(text="Saving", style="success.TButton")
        qrcode = pyqrcode.create(data_to_convert)
        name_file_to_save = str(filedialog.asksaveasfilename(
            filetypes=(
                ("", "*.png"),
            )
        ))
        name_file_to_save += ".png"
        if name_file_to_save.startswith(".png"):
            print("You have to chose a name")
            button1.configure(text="Submit", style='primary.TButton')
        else:
            qrcode.png(name_file_to_save, scale=20)
            os.startfile(name_file_to_save)
            print(name_file_to_save)
            button1.configure(text="Submit", style='primary.TButton')
    else:
        button1.configure(text="You Should Type Some Thing", style='danger.TButton')
# -----------End_func_2----------------

# Wifi Window
def wifi_window():
    # make the window and its properties
    global window2
    window2 = Toplevel(main_window)
    window2.config(bg="#f6f6f7")
    window2.grab_set()
    window2.geometry("380x380+{}+{}".format(postion(window2,380,380)[0],postion(window2,380,380)[1]))
    window2.title("QrCode Maker - Share Your Wifi Password")
    window2.resizable(False, False)
    window2.iconbitmap("AppIcon.ico")
    
    # Canvas Element to grid the other Elements
    canvas = tk.Canvas(window2, width=380, height=380, bg="#f6f6f7")
    canvas.grid(columnspan=2, rowspan=8)
    
    # Logo
    global logo_icon_s
    logo_icon_s = PhotoImage(file="Images/Logo_S.png")
    logo_icon_s.for_bug = logo_icon_s
    logo_window2 = Label(window2, image=logo_icon_s, bg="#f6f6f7")
    logo_window2.grid(column=0, columnspan=2, row=0)
    
    # Label 1
    lab1 = Label(window2, text="Wifi Password Share", font=("Comic Sans MS", 13, "bold"), bg="#f6f6f7")
    lab1.grid(column=0, row=1, columnspan=2)
    
    # Water Marks
    # 1
    water_mark_window2_1_photo = PhotoImage(file="Images/water_mark_5.png")
    water_mark_window2_1_photo.for_bug = water_mark_window2_1_photo
    water_mark_window2_1 = Label(window2, image=water_mark_window2_1_photo, bg="#f6f6f7")
    water_mark_window2_1.place(x=70, y=101)
    # 2
    water_mark_window2_2 = Label(window2, image=water_mark_photo_1, bg="#f6f6f7")
    water_mark_window2_2.place(x=-40, y=50)
    # 3
    water_mark_window2_3 = Label(window2, image=water_mark_photo_1, bg="#f6f6f7")    
    water_mark_window2_3.place(x=345, y=270)
    # 4
    water_mark_window2_4 = Label(window2, image=water_mark_photo_3, bg="#f6f6f7")
    water_mark_window2_4.place(x=26, y=169)
    # 5
    water_mark_window2_5 = Label(window2, image=water_mark_photo_4, bg="#f6f6f7")
    water_mark_window2_5.place(x=332, y=238)

    # label frame
    labelFrame2 = ttk.Labelframe(window2, text="Chose the network you want")
    labelFrame2.grid(column=0, row=3, padx=5, ipady=5, columnspan=2)
    
    # just to increase the width of labelframe
    canvas_2 = tk.Canvas(labelFrame2, width=300, height=0, highlightthickness=0, bg="#f6f6f7")
    canvas_2.grid(columnspan=2)
    
    # special var 1
    global wifi_selected
    wifi_selected = tk.StringVar(window2)
    
    # list to chose the SSID Name
    list_of_wifi_SSIDs = ttk.OptionMenu(labelFrame2, wifi_selected, "Select a network", *nameAndPass.keys())
    list_of_wifi_SSIDs.grid(column=0, row=3, padx=10, pady=5, sticky="NESW")
    
    # special var 2
    global is_hidden
    is_hidden = tk.IntVar(window2)

    # Check button to know if the network is hidden
    check_button = ttk.Checkbutton(labelFrame2, text="Hidden", variable=is_hidden
                                    , style="danger.TCheckbutton")
    s.configure("danger.TCheckbutton", font=("Comic Sans MS", 9))
    check_button.grid(column=1, row=3, pady=5)

    # Submit Button
    global submit_button
    submit_button = ttk.Button(window2, text='Submit', command=make_wifi_qr, width=25, style='primary.Outline.TButton')
    s.configure('primary.Outline.TButton', font=("Comic Sans MS", 13), background="#f6f6f7")
    submit_button.grid(column=0, row=6, columnspan=2)
# -----------End_func_3----------------

# Generate the wifi qrcode and open it for the user
def make_wifi_qr():
    # Get the SSID Chosen and put in a var just to not use .get() a lot
    SSID_chosen = wifi_selected.get()
    if SSID_chosen == "Select a network":
        # Change the color button and the text if user didn't chose a network
        submit_button.configure(text="Chose a network first", style='danger.Outline.TButton')
        s.configure('danger.Outline.TButton', font=("Comic Sans MS", 13))
    else:
        # retarn the button back whene user chose a network
        submit_button.configure(text="Submit", style='Outline.TButton')
        # _____________________________Organize vars and make theme ready to use____________________________

        # Get the value if network is hidden or not
        visibility = is_hidden.get()

        # Get the pass from our dic by the SSID_chosen
        password = nameAndPass.get(SSID_chosen)

        # Take the first value in password list just to put it in a normal str
        password = password[0]

        # Get the Type from our dic by the SSID_chosen
        security_type = nameAndType.get(SSID_chosen)
        
        # Take the first value in password list just to put it in a normal str
        security_type = security_type[0]
        

        if security_type[0:3] == "WPA":
            if visibility == 1:
                wifi_qrcode = pyqrcode.create("WIFI:S:" + SSID_chosen + ";T:WPA;P:" + password + ";H:true;")
            else:
                wifi_qrcode = pyqrcode.create("WIFI:S:" + SSID_chosen + ";T:WPA;P:" + password + ";;")
        elif security_type[0:3] == "WEB":
            if visibility == 1:
                wifi_qrcode = pyqrcode.create("WIFI:S:" + SSID_chosen + ";T:WEB;P:" + password + ";H:true;")
            else:
                wifi_qrcode = pyqrcode.create("WIFI:S:" + SSID_chosen + ";T:WEB;P:" + password + ";;")
        else:
            if visibility == 1:
                wifi_qrcode = pyqrcode.create("WIFI:S:" + SSID_chosen + ";T:nopass;P:;H:true;")
            else:
                wifi_qrcode = pyqrcode.create("WIFI:S:" + SSID_chosen + ";T:nopass;P:;;")
        name_of_wifi_file = str(filedialog.asksaveasfilename(
            filetypes=(
                ("", "*.png"),
            )
        ))
        name_of_wifi_file += ".png"
    if not name_of_wifi_file.startswith(".png"):
            wifi_qrcode.png(name_of_wifi_file, scale=20)
            os.startfile(name_of_wifi_file)
    logo_icon_s.for_bug = logo_icon_s
# -----------End_func_4----------------

# -------------------------------------------End Of Functions Area----------------------------------------

# ---------------------------------------Get The Wifi Name and Passwords----------------------------------

# make dic to store the Data
nameAndType = {}
nameAndPass = {}

# Get The SSID
wifiData = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

# put them in a list called profiles
SSID_name = [i.split(":")[1][1:-1] for i in wifiData if "All User Profile" in i]

# Get the pass for each of theme and store the SSID and pass in our dic nameAndPass
for i in SSID_name:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    nameAndPass[i] = results

# Get the Type of security for each of theme and store the SSID and typeOfSecurity in our dic nameAndType
for i in SSID_name:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    get_security_type = [b.split(":")[1][1:-1] for b in results if "Authentication" in b]
    nameAndType[i] = get_security_type
# ------------------------------------------------End--------------------------------------------------------

# Bootstrap Theme
S = ttkbootstrap.Style(theme='flatly')
s = ttk.Style()

# Make  Window
main_window = S.master
main_window.title("QrCode Maker")
main_window.resizable(False, False)
main_window.config(bg="#f6f6f7")

# put the window size and Positions the window in the center of the screen
main_window.geometry("450x500+{}+{}".format(postion(main_window,450,500)[0],postion(main_window,450,500)[1]))

# App Icon
main_window.iconbitmap("AppIcon.ico")
logo_icon_l = PhotoImage(file="Images/Logo_L.png")

# Frame 1
frame_1 = Frame(main_window, bg="#f6f6f7")
frame_1.pack()

# Logo
logo = Label(frame_1, image=logo_icon_l, bg="#f6f6f7")
logo.grid(column=0, row=0, columnspan=2, pady=15)

# NameOfLogo
nameOfLogo = Label(frame_1, text="Qrcode Maker", font=("Comic Sans MS", 15, "bold"), bg="#f6f6f7")
nameOfLogo.grid(column=0, row=1, columnspan=2, pady=10, sticky="NESW")

# Frame 2
frame_2 = Frame(main_window, bg="#f6f6f7")
frame_2.pack()

# ----------------------WaterMarks---------------------
# 1
water_mark_photo_1 = PhotoImage(file="Images/water_mark_1.png")
water_mark_1 = Label(main_window, image=water_mark_photo_1, bg="#f6f6f7")
water_mark_1.place(x=409, y=390)
# 2
water_mark_2 = Label(main_window, image=water_mark_photo_1, bg="#f6f6f7")
water_mark_2.place(x=-40, y=60)
# 3
water_mark_photo_2 = PhotoImage(file="Images/water_mark_2.png")
water_mark_3 = Label(main_window, image=water_mark_photo_2, bg="#f6f6f7")
water_mark_3.place(x=360, y=-22)
# 4
water_mark_photo_3 = PhotoImage(file="Images/water_mark_3.png")
water_mark_4 = Label(main_window, image=water_mark_photo_3, bg="#f6f6f7")
water_mark_4.place(x=-17, y=440)
# 5
water_mark_photo_4 = PhotoImage(file="Images/water_mark_4.png")
water_mark_5 = Label(main_window, image=water_mark_photo_4, bg="#f6f6f7")
water_mark_5.place(x=15, y=410)
# ---------------------------End-------------------------

# LabelFrame
labelFrame1 = ttk.Labelframe(frame_2, text="Enter Some Text Here:")
s.configure('TLabelframe.Label', font=("Comic Sans MS", 10), background="#f6f6f7")
s.configure('TLabelframe', background="#f6f6f7")
labelFrame1.grid(column=0, row=2, padx=8, pady=10, ipady=5)

# TextBox to get the data
textBoxOfData = Text(labelFrame1, width=50, height=8, font=("Comic Sans MS", 9))
textBoxOfData.grid(column=0, row=4, columnspan=2, padx=10, pady=5)

# button to perform the process
button1 = ttk.Button(frame_2, text="Make Qr-code", command=make_qr, style='TButton')
s.configure('TButton', font=("Comic Sans MS", 12), width=30)
button1.grid(column=0, row=5, columnspan=2, pady=5)

# button to open wifi sharing widow
button2 = ttk.Button(frame_2, text="Share Your WIFI Password", command=wifi_window, width=30, style='Outline.TButton')
s.configure('Outline.TButton', font=("Comic Sans MS", 10), background="#f6f6f7")
button2.grid(column=0, row=6, columnspan=2, padx=10, pady=5)

# copyright label
label2 = Label(frame_2, text="Copyright © 2021 Abdullah Sayed Sallam. All rights reserved", font=("Comic Sans MS", 8), bg="#f6f6f7")
label2.grid(column=0, row=7, columnspan=2, pady=7, sticky="NESW")

# to keep the window opened
main_window.mainloop()
