import socket
target=input("enter target to scan:")
print(f"\nscanning{target}...\n")
for port in range(1,1025):
    try:
        s=socket.socket()
        s.settimeout(0.5)
        s.connect((target,port))
        print(f"port{port} is open")
        s.close()
    except:
        pass
print("\nscan complete!")