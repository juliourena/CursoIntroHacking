# Ejemplo tomando del libro de Georgia Weidman

#!/usr/bin/python
import socket
ip = raw_input("Introduzca la IP: ")
port = input("Introduzca el Puerto: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if s.connect_ex((ip, port)):
  print "Puerto", port, "está cerrado"
else:
  print "Port", port, "está abierto"
