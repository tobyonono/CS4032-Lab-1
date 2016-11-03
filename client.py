import socket

socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.connect(("localhost", 8000))

sentence = ("Loughlin Lavery stole his lab 1 assignment")

print "Sent: "
socket1.send("GET /echo.php?message=" + sentence + "HTTP/1.1\r\n\r\n")

print "Received:"
data = socket1.recv(1024)

socket1.close()

print data
