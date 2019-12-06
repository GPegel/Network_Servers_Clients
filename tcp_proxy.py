#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import socket
import threading

def server_loop(local_host,local_port,remote_host,remote_port,receive_first):
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:

		server.bind((local_host,local_port))

	except:

		print "[!!] Failed to listen on %s:$d" % (local_host,local_port)
		print "[!!] Check for other listening sockets or correct permissions"
		sys.exit(0)

	print "[*] Listening on %s:%d" % (local_host,local_port)

	server.listen(5)

	while True:

		client_socket, addr = server.accept()

		# print out the local connection information
		print "[==>] Received incoming connection from %s:%d" % (addr[0],addr[1])

		# start a thread to talk to the remote host
		proxy_thread = threading.Thread(target=proxy_handler,
			args=(client_socket,remote_host,remote_port,receive_first))

		proxy_thread.start()

def main():

	# no fancy command-line parsing here
	if len(sys.argv[1:]) != 5:
		print "Usage: ./tcp_proxy.py [local host] [local port] [remote host] [remote port] [receive first]"
		print "Example: ./tcp_proxy.py 127.0.0.1 9000 10.12.132.1 9000 True"
		sys.exit(0)

	# setup local listening parameters
	local_host = sys.argv[1]
	local_port = int(sys.argv[2])

	# setup remote target
	remote_host = sys.argv[3]
	remote_port = int(sys.argv[4])

	# this tells our proxy to connect and receive data before sending to the remomte host
	receive_first = sys.argv[5]

	if "True" in receive_first:
		receive_first = True
	else:
		receive_first = False

	# now spin up our listening socket
	server_loop(local_host,local_port,remote_host,remote_port,receive_first)

main()
