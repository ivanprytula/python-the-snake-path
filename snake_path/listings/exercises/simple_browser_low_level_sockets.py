import socket

# prepare socket
my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#                   Host         Port
print(type(my_sock))  # <class 'socket.socket'>

my_sock.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
my_sock.send(cmd)  # sends bytes

while True:
    data = my_sock.recv(512)  # receives bytes

    if len(data) < 1:
        break

    print(data.decode(), end='')  # from bytes to utf-8
my_sock.close()
"""
HTTP/1.1 200 OK
Date: Mon, 30 Aug 2021 23:40:58 GMT
Server: Apache/2.4.18 (Ubuntu)
Last-Modified: Sat, 13 May 2017 11:22:22 GMT
ETag: "a7-54f6609245537"
Accept-Ranges: bytes
Content-Length: 167
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Connection: close
Content-Type: text/plain

But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief

Process finished with exit code 0

"""

# UTF-8 -> 1-4 bytes, dynamic length
