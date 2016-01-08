# check_certificate.py 1.0
# Marquis Montgomery, Senior Security Consultant
# Splunk Inc. Security Services and Solutions

# Uses the openssl binary to check the expiration date of the public certificate served by list of remote hosts.

HOW TO USE:
1) Confirm the openssl command works on your system.
2) Update hostList.txt with the server:port of the SSL services you'd like to get the expiry dates of
3) run 'python check_certificate.py'

Note: This is a very basic script with no error/exception handling.

