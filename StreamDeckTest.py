
import customtkinter as ctk
from PIL import Image, ImageTk
import pyautogui
import time


window = ctk.CTk()
window._set_appearance_mode("dark")
window.title("Atena Tech")
window.geometry("700x500")
window.maxsize(width=900, height=550)
window.minsize(width=700, height=400)
window.resizable(width=True, height=False)


def button01_event():
    pyautogui.hotkey('win')
    pyautogui.typewrite('spotify')
    pyautogui.hotkey('enter')


def button02_event():
    pyautogui.hotkey('win')
    pyautogui.typewrite('Figma')
    pyautogui.hotkey('enter')


def button03_event():
    pyautogui.moveTo(1750, 1060)
    pyautogui.click()
    pyautogui.moveTo(1592, 1012)
    pyautogui.click()


def button04_event():
    pyautogui.hotkey("win")
    pyautogui.typewrite("Epic Games")
    pyautogui.hotkey('Enter')


def button05_event():
    pyautogui.hotkey("win")
    pyautogui.typewrite("Adobe Premiere")
    pyautogui.hotkey('Enter')


def button06_event():
    pyautogui.hotkey("win")
    pyautogui.typewrite('spotify')
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.moveTo(909, 979)
    pyautogui.click()
    pyautogui.click()


def button07_event():
    pyautogui.hotkey('win')
    pyautogui.typewrite('Opera')
    pyautogui.hotkey('Enter')
    pyautogui.hotkey('ctrl', 't')
    pyautogui.typewrite('drive.google.com')
    pyautogui.hotkey('enter')


def button08_event():
    pyautogui.hotkey('win')
    pyautogui.typewrite('cmd')
    pyautogui.hotkey('Enter')
    pyautogui.typewrite('shutdown -s')


def button09_event():
    pyautogui.hotkey("win")
    pyautogui.typewrite('spotify')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('space')


def button10_event():  # Corrigir
    pyautogui.hotkey("win")
    pyautogui.typewrite('spotify')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('space')


def button11_event():
    pyautogui.hotkey("win")
    pyautogui.typewrite('Photoshop')
    pyautogui.hotkey('enter')


def button12_event():
    pyautogui.hotkey("win")
    pyautogui.typewrite('spotify')
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'arrow right')


def button13_event():
    pyautogui.hotkey("win")
    pyautogui.typewrite('Opera')
    pyautogui.hotkey('enter')


def button14_event():
    pyautogui.hotkey('win')
    pyautogui.typewrite('Opera')
    pyautogui.hotkey('enter')
    pyautogui.typewrite('mail.google.com')


def button15_event():
    pyautogui.hotkey('win')
    pyautogui.typewrite('Spotify')
    pyautogui.hotkey('ctrl', 'r')


    # Custom Config Colors / Aparence
ctk.set_default_color_theme("CustomCG.json")


# Label
ctk.CTkLabel(window, text=" AtenaDev Deck",
             font=("Roboto Bold", 20), bg_color="#242424", text_color='#fff').pack(pady=20, padx=5)


# Images Buttons

image01 = ctk.CTkImage(Image.open("test-images/spotify.png"), size=(64, 64))
image02 = ctk.CTkImage(Image.open("test-images/Figma.png"), size=(64, 64))
image03 = ctk.CTkImage(Image.open("test-images/Mute.png"), size=(64, 64))
image04 = ctk.CTkImage(Image.open("test-images/Game.png"), size=(64, 64))
image05 = ctk.CTkImage(Image.open("test-images/Premiere.png"), size=(64, 64))
image06 = ctk.CTkImage(Image.open("test-images/Back.png"), size=(64, 64))
image07 = ctk.CTkImage(Image.open("test-images/Drive.png"), size=(64, 64))
image08 = ctk.CTkImage(Image.open("test-images/Power.png"), size=(64, 64))
image09 = ctk.CTkImage(Image.open("test-images/Pause.png"), size=(64, 64))
image10 = ctk.CTkImage(Image.open("test-images/Mail.png"), size=(64, 64))
image11 = ctk.CTkImage(Image.open("test-images/Photoshop.png"), size=(64, 64))
image12 = ctk.CTkImage(Image.open("test-images/Foward.png"), size=(64, 64))
image13 = ctk.CTkImage(Image.open("test-images/OperaGX.png"), size=(64, 64))
image14 = ctk.CTkImage(Image.open("test-images/Youtube.png"), size=(64, 64))
image15 = ctk.CTkImage(Image.open("test-images/Repeat.png"), size=(64, 64))

# Buttons

# 1 Coluna

button01 = ctk.CTkButton(
    master=window, width=64, height=64, text='',  image=image01, bg_color='#EBEBEB', command=button01_event).place(x=100, y=100)

button02 = ctk.CTkButton(
    master=window, width=64, height=64, text='',  image=image02, bg_color='#EBEBEB', command=button02_event).place(x=100, y=200)

button03 = ctk.CTkButton(
    master=window, width=64, height=64, text='',  image=image03, bg_color='#EBEBEB', command=button03_event).place(x=100, y=300)


# 2 Coluna

button04 = ctk.CTkButton(
    master=window, width=64, height=64, text='',  image=image04, bg_color='#EBEBEB', command=button04_event).place(x=200, y=100)

button05 = ctk.CTkButton(
    master=window, width=64, height=64, text='',  image=image05, bg_color='#EBEBEB', command=button05_event).place(x=200, y=200)

button06 = ctk.CTkButton(
    master=window, width=64, height=64, text='',  image=image06, bg_color='#EBEBEB', command=button06_event).place(x=200, y=300)


# 3 Coluna

button07 = ctk.CTkButton(
    master=window, width=64, height=64, text='',  image=image07, bg_color='#EBEBEB', command=button07_event).place(x=300, y=100)

button08 = ctk.CTkButton(
    master=window, width=64, height=64, text='',  image=image08, bg_color='#EBEBEB', command=button08_event).place(x=300, y=200)

button09 = ctk.CTkButton(
    master=window, width=64, height=64, text='',  image=image09, bg_color='#EBEBEB', command=button09_event).place(x=300, y=300)

# 4 Coluna

button10 = ctk.CTkButton(
    master=window, width=64, height=64, text='',  image=image10, bg_color='#EBEBEB', command=button10_event).place(x=400, y=100)

button11 = ctk.CTkButton(
    master=window, width=64, height=64, text='',  image=image11, bg_color='#EBEBEB', command=button11_event).place(x=400, y=200)

button12 = ctk.CTkButton(
    master=window, width=64, height=64, text='',  image=image12, bg_color='#EBEBEB', command=button12_event).place(x=400, y=300)


# 5 Coluna

button13 = ctk.CTkButton(
    master=window, width=64, height=64, text='',  image=image13, bg_color='#EBEBEB', command=button13_event).place(x=500, y=100)

button14 = ctk.CTkButton(
    master=window, width=64, height=64, text='',  image=image14, bg_color='#EBEBEB', command=button14_event).place(x=500, y=200)

button15 = ctk.CTkButton(
    master=window, width=64, height=64, text='',  image=image15, bg_color='#EBEBEB', command=button15_event).place(x=500, y=300)


window.mainloop()
