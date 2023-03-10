# Easy Client Connections

# TCP/IP clients can save a few steps by using the convenience function create_connection() to connect to a server. The function takes one argument, a two-value tuple containing the address of the server, and derives the best address to use for the connection.

import socket
import sys


def get_constants(prefix):
    """Create a dictionary mapping socket module constants to their names."""
    return dict((getattr(socket, n), n)
                for n in dir(socket)
                if n.startswith(prefix)
                )


families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

# Create a TCP/IP socket
sock = socket.create_connection(('localhost', 10000))

print >> sys.stderr, 'Family  :', families[sock.family]
print >> sys.stderr, 'Type    :', types[sock.type]
print >> sys.stderr, 'Protocol:', protocols[sock.proto]
print >> sys.stderr

try:

    # Send data
    message = 'This is the message.  It will be repeated.'
    print >> sys.stderr, 'sending "%s"' % message
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print >> sys.stderr, 'received "%s"' % data

finally:
    print >> sys.stderr, 'closing socket'
    sock.close()

# create_connection() uses getaddrinfo() to find candidate connection parameters, and returns a socket opened with the first configuration that creates a successful connection. The family, type, and proto attributes can be examined to determine the type of socket being returned.

