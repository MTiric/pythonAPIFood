import socket

import methods

HOST = "192.168.1.4"
PORT = 65432
HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")


    # Receive date and time from the client
    datetime_string = clientsocket.recv(1024).decode("utf-8")
    print(f"Received date and time from client: {datetime_string}")
    res = eval(datetime_string)
    print("Tuple after conversion : " + str(res))

    try:
        time_difference = methods.calculate_time_difference_in_minutes(res[0], res[1])
        print(f"Successful calculation, time diff: {time_difference}")
        datetime_string = f"{time_difference}"
    except:
        time_difference = ""
        print("Unsuccessful calculation")

    clientsocket.send(bytes(datetime_string, "utf-8"))
    clientsocket.close()
