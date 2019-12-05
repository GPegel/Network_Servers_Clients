import sys
import socket
import getopt
import threading
import subprocess

# define some global variables
listen					= False
command					= False
upload 					= False
execute					= ""
target					= ""
upload_destination			= ""
port					= 0

def usage():
	print "CatNet - A sort of NetCat tool"
	print
	print "Usage: catnet.py -t target_host -p port"
	print "-l --listen				- listen on [host]:[port] for incoming connections"
	print "-e --execute=file_to_run		- execute the given file upn"
	print "-c --command 				- initialize a command shell"
	print "-u --upload=destination 		- upon receiving connection upload a file and write to [destination]"
	print
	print
	print "Examples"
	print "catnet.py -t 192.168.178.1 -p 5555 -l -c"
	print "catnet.py -t 192.168.178.1 -p 5555 -l -u=c:\\target.exe"
	print "catnet.py -t 192.168.178.1 -p 5555 -l -e\"cat /etc/passwd\""
	print "echo 'Say Cheese... | ./catnet.py -t 192.168.188.11 -p 135" 
	sys.exit(0)

def main():
	global listen
	global command
	global upload
	global execute
	global target
	global upload_destination

	if not len(sys.argv[1:]):
		usage()

	# read the commandline options
	try:
		opts, args = getopt.getopt(sys.argv[1:],"hle:t:p:cu:", ["help","listen","execute","target","port","command","upload"])

	except getopt.GetoptError as err:
		print str(err)
		usage()

	for o,a in opts:
		if o in ("-h","--help"):
			usage()
		elif o in ("-l","--listen"):
			listen = True
		elif o in ("-e", "--execute"):
			execute = a
		elif o in ("-c", "--commandshell"):
			command = True
		elif o in ("-u", "--upload"):
			upload_destination = a
		elif o in ("-t", "--target"):
			target = a
		elif o in ("-p", "--port"):
			port = int(a)
		else:
			assert False,"Unhandled Option"

	# are we going to listen or just send data from stdin?

	if not listen and len(target) and port > 0:

	# read in the buffer from the CLI this will block, so cent CTRL-D if not sending input

	# to stdin
		buffer = sys.stdin.read()

	# send data off
		client_sender(buffer)

	# we are going to listen and potentially upload thingies, execute commands and drop a shell back
	# depending on our command line options above

	if listen:
		server_loop()

main()

