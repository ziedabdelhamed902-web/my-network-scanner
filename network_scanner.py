import socket
def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is OPEN!")
        else:
            print(f"Port {port} is CLOSED")
        s.close()
    except:
        pass
ports_to_scan = [22, 80, 443, 445, 3389]
for p in ports_to_scan:
    scan_port("192.168.75.2", p)
