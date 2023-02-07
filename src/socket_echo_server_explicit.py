# Choosing an Address for Listening

# It is important to bind a server to the correct address, so that clients can communicate with it. The previous examples all used 'localhost' as the IP address, which limits connections to clients running on the same server. Use a public address of the server, such as the value returned by gethostname(), to allow other hosts to connect. This example modifies the echo server to listen on an address specified via a command line argument.

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_name = sys.argv[1]
server_address = (server_name, 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
sock.listen(1)


# Bind the socket to the address given on the command line
# Many servers have more than one network interface, and therefore more than one IP address. Rather than running separate copies of a service bound to each IP address, use the special address INADDR_ANY to listen on all addresses at the same time. Although socket defines a constant for INADDR_ANY, it is an integer value and must be converted to a dotted-notation string address before it can be passed to bind(). As a shortcut, use the empty string '' instead of doing the conversion.

# server_address = ('', 10000)
# sock.bind(server_address)
# print >>sys.stderr, 'starting up on %s port %s' % sock.getsockname()
# sock.listen(1)

while True:
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'client connected:', client_address
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'received "%s"' % data
            if data:
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()