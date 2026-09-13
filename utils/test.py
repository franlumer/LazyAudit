import re

command = "nmap -p- -T4 {RHOST}"

#string = re.search("{.*}", command)
string = re.sub("{.*}", "192.168.0.1", command)

print(string)