import socket
import os 
from threading import Thread

discovered_hosts = []

def scan_port(ip, port, scan_path):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.3)
        if sock.connect_ex((ip, port)) == 0:
            if ip not in discovered_hosts:
                discovered_hosts.append(ip)
                with open(os.path.join(scan_path, "targets_found.txt"), "a") as f:
                    f.write(f"Host: {ip} | Port: {port}\n")

def start_scan(base_ip, scan_path):
    threads = []
    ports = [22, 80, 445, 3389] 
    
    for i in range(1, 255):
        ip = f"{base_ip}.{i}"
        for p in ports:
            t = Thread(target=scan_port, args=(ip, p, scan_path))
            t.start()
            threads.append(t)
    
    for t in threads:
        t.join()
        
    return discovered_hosts