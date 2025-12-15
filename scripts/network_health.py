import subprocess
import platform
import logging
import socket

logging.basicConfig(filename='../logs/automation.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

REMOTE_SERVER = "8.8.8.8"
DNS_HOST = "google.com"

def ping_check(host):
    """
    Returns True if host (str) responds to a ping request.
    """
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]
    
    try:
        # Suppress output to keep console clean
        subprocess.check_call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def check_dns(hostname):
    """
    Checks if DNS resolution works for a hostname.
    """
    try:
        socket.gethostbyname(hostname)
        return True
    except socket.error:
        return False

def main():
    print("--- Network Health Check ---")
    
    # 1. Ping Check
    if ping_check(REMOTE_SERVER):
        print(f"[OK] Connectivity to {REMOTE_SERVER} is active.")
        logging.info(f"Ping check passed for {REMOTE_SERVER}")
    else:
        print(f"[FAIL] Cannot reach {REMOTE_SERVER}. Check internet connection.")
        logging.error(f"Ping check failed for {REMOTE_SERVER}")

    # 2. DNS Check
    if check_dns(DNS_HOST):
        print(f"[OK] DNS resolution for {DNS_HOST} is working.")
        logging.info(f"DNS check passed for {DNS_HOST}")
    else:
        print(f"[FAIL] DNS resolution failed for {DNS_HOST}.")
        logging.error(f"DNS check failed for {DNS_HOST}")

if __name__ == "__main__":
    main()