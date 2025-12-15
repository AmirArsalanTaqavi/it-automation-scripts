import shutil
import argparse
import sys
import os
import logging

# Configure logging
logging.basicConfig(filename='../logs/automation.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_args():
    parser = argparse.ArgumentParser(description="Monitor disk usage of a specific path.")
    parser.add_argument("--path", type=str, default="/", help="Path to check disk usage for (default: /)")
    parser.add_argument("--threshold", type=int, default=80, help="Disk usage percentage threshold for warning (default: 80)")
    return parser.parse_args()

def check_disk_usage(path):
    """Returns the disk usage percentage."""
    try:
        total, used, free = shutil.disk_usage(path)
        percent_used = (used / total) * 100
        return percent_used
    except FileNotFoundError:
        logging.error(f"Path not found: {path}")
        print(f"Error: Path '{path}' does not exist.")
        sys.exit(1)
    except Exception as e:
        logging.error(f"Error checking disk usage: {e}")
        print(f"Error: {e}")
        sys.exit(1)

def main():
    args = get_args()
    path = args.path
    threshold = args.threshold

    print(f"Checking disk usage for: {path}")
    usage = check_disk_usage(path)

    print(f"Current Usage: {usage:.2f}%")
    print(f"Threshold: {threshold}%")

    if usage > threshold:
        msg = f"WARNING: Disk usage on '{path}' is above threshold! ({usage:.2f}%)"
        print(msg)
        logging.warning(msg)
    else:
        msg = f"Disk usage on '{path}' is within safe limits."
        print(msg)
        logging.info(msg)

if __name__ == "__main__":
    main()