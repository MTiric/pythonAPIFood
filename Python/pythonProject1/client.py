import socket
import threading

HOST = "192.168.1.6"
PORT = 65432
HEADERSIZE = 10


def send_time(datetime_string):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    # Send date and time to the server

    print(f"Sent date and time: {datetime_string}")
    s.send(bytes(datetime_string, "utf-8"))
    # receive_Thread.start()

    return received_difference(s)

def received_difference(s):
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect((HOST, PORT))
    message_content = True
    while message_content:
        full_msg = ''
        new_msg = True

        while message_content:
            msg = s.recv(16)

            full_msg += msg.decode("utf-8")
            print(full_msg)

            print("msg recvd")
            message_content = False

        print(full_msg)
        return full_msg


receive_Thread = threading.Thread(target=received_difference)

