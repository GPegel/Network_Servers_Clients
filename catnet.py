import sys
import socket
import getopt
import threading
import subprocess

# define some global variables
listen                  = False
command                 = False
upload                  = False
execute                 = ""
target                  = ""
upload_destination      = ""
port                    = 0

def usage():
    print "CatNet - A sort of NetCat tool"
    print
    print "Usage: catnet.py -t target_host -p port"
    print "-l --listen                  - listen on [host]:[port] for incoming connections"
    print "-e --execute=file_to_run     - execute the given file upn"
    print "-c --command                 - initialize a command shell"
    print "-u --upload=destination      - upon receiving connection upload a file and write to [destination]"
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

def client_sender(buffer):

    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:

        # connect to our target host
        client.connect((target_port))

        if len(buffer):
            client.send(buffer)

        while True:

            # now wait for data back
            recv_len = 1
            response = ""

            while recv_len:
                data = client.recv(4096)
                recv_len = len(data)
                response += data

                if recv_len < 4096:
                    break
            print response,

            # wait for more input
            buffer = raw_input("")
            buffer += "\n"

            # send it off
            client.send(buffer)
    
    except:

        print "[*] Exception! Exitng."

        # tear down the connection
        clientclose()

def server_loop():
    global target

    # if no target is defined, we listen on all interfaces

    if not len(target):
        target = "0.0.0.0"

    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((target,port))
    server.listen(5)

    while True:
        client_socket, addr = server.accept()

        # spin off a thread to handle our new client

        client_thread = threading.Thread(target=client_handler,args=(client_socket,))
        client_thread.start()

def run_command(command):

    # trim the newline
    command = command.rstrip()

    # run the command and get the output back
    try:
        output = subprocess.check_output(command,stderr=subprocess.STDOUT, shell=True)
    except:
        output = "Failed to execute command.\r\n"
    # send the output back to the client
    return output

main()



