# imports
import socket
import sys
import os
import datetime

# function: send tcp message to target
def send(ip, port, mesg, outfile):

	# get timestamp
	ct = datetime.datetime.now()

	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Connect the socket to the port where the server is listening
	target = (ip, port)

	#print(f'Connecting to port {port} at {ip}')
	sock.connect(target)

	# send data
	try:

		# clear the screen
		os.system('clear')

		# print and write to file
		print(f'Sending message: {mesg}') 
		outfile.write(f'Sending to IP:{ip}, port:{str(port)}, time:{ct}\n')
		outfile.write(f'Sending message: {mesg}\n')

		# encode the message as byte string
		mesg = mesg.encode()

		# send the message
		sock.sendall(mesg)

		# receive response
		data = sock.recv(1024)

		# print and write response to file
		print(f'Received response: {data}')
		outfile.write(f'Received response: {data}\n')

	# close socket
	finally:
		outfile.write('\n')
		sock.close()

# main function
def main(argv):

	# error checking input
	if len(argv) != 4:
		print("Usage: <script> <IP> <port>")
		quit()
	else:
		# set command line variables
		ip = argv[1]
		port = int(argv[2])
		message = argv[3]

	# open log file for append
	with open('tcp_log.txt', 'a') as outfile:

		# call function
		send(ip, port, message, outfile)

# start program
if __name__ == '__main__':
	main(sys.argv)