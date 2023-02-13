import socket

def start_client():
    host = "127.0.0.1"
    port = 5000

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    while True:
        command = input("Enter command (left_click, right_click, move_mouse x y, drag_mouse x y, scroll n, press_key key, hotkey key1 key2 ...): ")
        client.send(command.encode("utf-8"))

if __name__ == "__main__":
    start_client()
