from subprocess import Popen, PIPE
import sys

# arp -a output - on mac and linux
"""
? (192.168.1.1) at 3c:37:86:47:cd:85 on en0 ifscope [ethernet]
? (192.168.1.13) at 1c:f2:9a:1f:1a:6c on en0 ifscope [ethernet]
? (192.168.1.21) at 0:c3:f4:45:70:8c on en0 ifscope [ethernet]
"""
# sys.platform returns the local device OS
# if the local device is mac
if sys.platform.startswith("darwin"):
    # seding arp commad to the local device
    arp = Popen(["arp", "192.168.1.1"], stdout=PIPE, stderr=PIPE)
# if the local device is linux
elif sys.platform.startswith("linux"):
    arp = Popen(["arp", "192.168.1.1"], stdout=PIPE, stderr=PIPE)
else:
    print("IF WINDOWS, GO AWAY!!!")
# will get an output or error message
output, err = arp.communicate()
# if error break out of the script and print error
if err:
    sys.exit(err)
# 0 means that the command return an output
if arp.returncode == 0:
    print(output)
else:
    print("IP NOT FOUND")
