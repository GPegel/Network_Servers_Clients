# Network_Servers_Clients
TCP and UDP clients and servers written in Python

## Simple TCP Client
tcp_client.py

## Simple UDP Client
udp_client.py

## Multi-Threaded TCP Server
tcp_server.py

When launching this server, it will start a server running on localhost and port 9999. When visiting this server in a browser you will get a response like this:

```
[*] Listening on 0.0.0.0:9999
[*] Accepted connection from: 127.0.0.1:61607
[*] Received: GET / HTTP/1.1
Host: 0.0.0.0:9999
Upgrade-Insecure-Requests: 1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15
Accept-Language: en-us
Accept-Encoding: gzip, deflate
Connection: keep-alive

[*] Accepted connection from: 127.0.0.1:61609
[*] Received: GET / HTTP/1.1
Host: 0.0.0.0:9999
Upgrade-Insecure-Requests: 1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15
Accept-Language: en-us
Accept-Encoding: gzip, deflate
Connection: keep-alive


[*] Accepted connection from: 127.0.0.1:61611
[*] Received: GET / HTTP/1.1
Host: 0.0.0.0:9999
Upgrade-Insecure-Requests: 1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15
Accept-Language: en-us
Accept-Encoding: gzip, deflate
Connection: keep-alive
```