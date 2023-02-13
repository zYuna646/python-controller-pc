import socket
import pyautogui

def start_server():
    host = "127.0.0.1"
    port = 5000
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)

    print("Server started... waiting for clients...")

    client_socket, client_address = server.accept()
    print("Client connected:", client_address)

    while True:
        data = client_socket.recv(1024).decode("utf-8")
        if not data:
            break

        if data == "left_click":
            pyautogui.click()
        elif data == "right_click":
            pyautogui.click(button="right")
        elif data.startswith("move_mouse"):
            x, y = map(int, data.split(" ")[1:])
            pyautogui.moveTo(x, y)
        elif data.startswith("drag_mouse"):
            x, y = map(int, data.split(" ")[1:])
            pyautogui.dragTo(x, y)
        elif data.startswith("scroll"):
            scroll = int(data.split(" ")[1])
            pyautogui.scroll(scroll)
        elif data.startswith("press_key"):
            key = data.split(" ")[1]
            pyautogui.press(key)
        elif data.startswith("hotkey"):
            keys = data.split(" ")[1:]
            pyautogui.hotkey(*keys)

    client_socket.close()
    server.close()

if __name__ == "__main__":
    start_server()
