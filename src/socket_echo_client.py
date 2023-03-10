# Echo Client
# The client program sets up its socket differently from the way a server does. Instead of binding to a port and listening, it uses connect() to attach the socket directly to the remote address.

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

#After the connection is established, data can be sent through the socket with sendall() and received with recv(), just as in the server.
try:

    # Send data
    message = 'This is the message.  It will be repeated.'
    print >> sys.stderr, 'sending "%s"' % message
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print >> sys.stderr, 'received "%s"' % data

finally:
    print >> sys.stderr, 'closing socket'
    sock.close()

# When the entire message is sent and a copy received, the socket is closed to free up the port.


# TESTING socket_echo_client_explicit.py
# A similar modification to the client program is needed before the server can be tested.

# import socket
# import sys
#
#Create a TCP/IP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
#Connect the socket to the port on the server given by the caller
# server_address = (sys.argv[1], 10000)
# print >> sys.stderr, 'connecting to %s port %s' % server_address
# sock.connect(server_address)
#
# try:
#
#     message = 'This is the message.  It will be repeated.'
#     print >> sys.stderr, 'sending "%s"' % message
#     sock.sendall(message)
#
#     amount_received = 0
#     amount_expected = len(message)
#     while amount_received < amount_expected:
#         data = sock.recv(16)
#         amount_received += len(data)
#         print >> sys.stderr, 'received "%s"' % data
#
# finally:
#    sock.close()

