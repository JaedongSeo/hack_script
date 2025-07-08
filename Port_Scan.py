import socket
import sys


target = input("Target Ip: ")
ports = [21,22,23,25,53,80,443,3306,8080]

print(f"\n[*] Scanning {target}...")

for port in ports:
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((target,port))
        print(f"[+] Port {port}is open")
    except:
        pass
    finally:
        s.close()


