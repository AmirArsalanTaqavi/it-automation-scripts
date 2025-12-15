import psutil
import logging

logging.basicConfig(filename='../logs/automation.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

CRITICAL_SERVICES = ['cron', 'nginx', 'docker', 'ssh']

def check_service_status(service_name):
    for proc in psutil.process_iter(['name']):
        if service_name in proc.info['name']:
            return True
    return False

def main():
    print("--- Service Status Checker ---")
    for service in CRITICAL_SERVICES:
        is_running = check_service_status(service)
        status = "RUNNING" if is_running else "STOPPED"
        print(f"Service '{service}': {status}")
        
        if not is_running:
            logging.warning(f"Alert: Service {service} is not running!")
        else:
            logging.info(f"Service {service} is active.")

if __name__ == "__main__":
    main()