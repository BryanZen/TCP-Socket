Sending information across the network requires creating a connection and then sending data
over this connection. Your goal is to write an application that creates a connection and then
write an application protocol on top of it.

Here is an example for you to create a client and server socket. This is a “TCP” socket. You will
learn more about this after the application layer classes. https://pymotw.com/2/socket/tcp.html
The above example is an echo server that echoes the client question. Try instead to write an
application and create a protocol for the application

Application Description:

• The Addressbook service is a client-server application. A client sends a query message to
the server containing an email address. The server responds to the client with a
message that contains the full name which corresponds to the email address.

• The following messages format is used for query and response:
Message Type (1 byte)
Length String (1 byte)
Question/Response (<=255 bytes)

• Message Type is set to “Q” for queries, and “R” for responses.

• The server runs on a known address and listens on a well-known port. For now assume
you are running both the server and client on the local host similar to the example
above.

<img width="523" alt="example" src="https://user-images.githubusercontent.com/91381333/217129799-0f6a1c6a-ab7c-4748-9764-1b43c03ba2b8.png">
