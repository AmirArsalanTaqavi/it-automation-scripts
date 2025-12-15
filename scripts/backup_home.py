import shutil
import datetime
import os
import logging

logging.basicConfig(filename='../logs/automation.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# تنظیمات
SOURCE_DIR = "/home/user/documents"  # Path
BACKUP_DIR = "/tmp/backups"

def create_backup():
    if not os.path.exists(SOURCE_DIR):
        print(f"Error: Source directory {SOURCE_DIR} not found.")
        return

    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    date_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    archive_name = os.path.join(BACKUP_DIR, f"backup_{date_str}")
    
    try:
        shutil.make_archive(archive_name, 'zip', SOURCE_DIR)
        print(f"Backup created successfully: {archive_name}.zip")
        logging.info(f"Backup created: {archive_name}.zip")
    except Exception as e:
        print(f"Backup failed: {e}")
        logging.error(f"Backup failed: {e}")

if __name__ == "__main__":
    create_backup()