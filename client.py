import socket

socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.connect(("localhost", 8000))

sentence = "testing12"
socket1.send("GET /echo.php?message=" + sentence + " HTTP/1.1\r\n\r\n")

print "Received:"
data = socket1.recv(2048)

socket1.close()

print data
