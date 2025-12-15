import psutil
import platform
import logging

logging.basicConfig(filename='../logs/automation.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_system_info():
    info = {
        "System": platform.system(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "CPU Cores": psutil.cpu_count(logical=True),
        "RAM Total (GB)": round(psutil.virtual_memory().total / (1024**3), 2)
    }
    return info

def main():
    try:
        print("--- System Information ---")
        info = get_system_info()
        for key, value in info.items():
            print(f"{key}: {value}")
        
        logging.info("System info retrieved successfully.")
    except Exception as e:
        logging.error(f"Error fetching system info: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()