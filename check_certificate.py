# check_certificate.py 1.0
# Marquis Montgomery, Senior Security Consultant
# Splunk Inc. Security Services and Solutions

# Uses the openssl binary to check the expiration date of the public certificate served by list of remote hosts.

import fileinput
import sys
import subprocess

serverList = []
hostFile = open("hostList.txt")
hostList = hostFile.readlines()

for i in hostList:
	i = i.rstrip()
	print "*** Getting OpenSSL Certificate Expiry for %s" % (i)
	command = "echo | openssl s_client -connect %s 2>/dev/null | openssl x509 -noout -enddate" % (i)
	print subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()