#!/usr/bin/python

###########################################
#                                         #
# Metasploit Resource File Creator (SNMP) #
# By cy7he                                #
#                                         #
###########################################

import sys, subprocess

def usage():
	print "Usage: %s <hosts>" %sys.argv[0]
	exit()

if(len(sys.argv) < 2):
	usage()

hosts = sys.argv[1]

resource = open("snmp.rc", "w")
resource.write("use auxiliary/scanner/snmp/snmp_enum\n")
resource.write("set RHOSTS " + hosts + "\n")
resource.write("set THREADS 10" + "\n")
resource.write("run")
resource.close()

subprocess.Popen('sudo msfconsole -r snmp.rc', shell=True).wait()
