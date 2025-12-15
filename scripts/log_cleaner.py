import os
import time
import logging

logging.basicConfig(filename='../logs/automation.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

LOG_DIR = "/tmp/logs_test"  # specify path
DAYS_TO_KEEP = 7

def clean_old_logs():
    if not os.path.exists(LOG_DIR):
        print(f"Directory {LOG_DIR} does not exist.")
        return

    now = time.time()
    cutoff = now - (DAYS_TO_KEEP * 86400)
    deleted_count = 0

    print(f"Cleaning logs older than {DAYS_TO_KEEP} days in {LOG_DIR}...")
    
    for filename in os.listdir(LOG_DIR):
        file_path = os.path.join(LOG_DIR, filename)
        if os.path.isfile(file_path):
            file_mtime = os.path.getmtime(file_path)
            if file_mtime < cutoff:
                try:
                    os.remove(file_path)
                    print(f"Deleted: {filename}")
                    deleted_count += 1
                except Exception as e:
                    print(f"Error deleting {filename}: {e}")
    
    print(f"Total files deleted: {deleted_count}")
    logging.info(f"Log cleanup completed. Deleted {deleted_count} files.")

if __name__ == "__main__":
    clean_old_logs()