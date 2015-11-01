#!/usr/bin/python

# Usage: python Python-TraceTester.py <host> <port>
# Author: Jamie Shaw @jlshaw87

import socket, sys, os

os.system("clear")

print "TRACE Method Verfication"
print "      Author: Jamie Shaw"

target = sys.argv[1]
port = sys.argv[2]

header_method = "TRACE / HTTP/1.1"
header_payload = "Test: <script>alert('TRACE');</script>"
header_host = "Host: %s" %(target)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex( (target,int(port)) )
sock.settimeout(5)

if result == 0:
	print '\n[+] Testing, please wait...\n'
	sock.send(header_method + "\n")
	sock.send(header_payload + "\n")
	sock.send(header_host + "\n\n")
	data = sock.recv(1024)
	if '200 OK' in data:
		print "%s:%s  -  Appears to have the TRACE method enabled.\n" %(target, port)
		print "HTTP Response output below:\n"
		print data
	else:
		print "%s:%s  -  Does not appear to have the TRACE method enabled.\n" %(target, port)
else:
		print "\tUnable to establish connection to %s:%s\n" %(target, port)

sock.close()
