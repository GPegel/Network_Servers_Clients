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
upload_destination		= ""
port					= 0

def usage():
	print "CatNet - A sort of NetCat tool"
	print
	print "Usage: catnet.py				-t taget_host -p port"
	print "-l --listen					- listen on [host]:[port] for incoming connections"
	print "-e --execute=file_to_run		- execute the given file upn"
	print "-c --command					- initialize a command shell"
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