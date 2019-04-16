import socket
import subprocess
import platform

name = "pyICMP"


def ping(address, count=4, ttl=255):
    
    #validate ip address
    try:
        socket.gethostbyname(address)
    except:
        raise ValueError("IP address or DNS name not valid")
    
    #get to pinging

    #detect os and set command in cmd var
    cmd = ["ping", "-c", str(count), address, '-t', str(ttl)]
    if platform.system() == 'Windows':
        cmd = ["ping", "-n", str(count), address]
    
    failed = subprocess.call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    #Assume it was sucessful
    r = True

    #if it failed change the var
    if failed:
        r = False
    
    return r

def traceroute(address):
    pass