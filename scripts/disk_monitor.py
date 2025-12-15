import shutil

# Configuration
PATH = "/"
THRESHOLD = 80  # percent

def check_disk_usage(path):
    total, used, free = shutil.disk_usage(path)
    percent_used = (used / total) * 100
    return percent_used

def main():
    usage = check_disk_usage(PATH)

    print(f"Disk usage on {PATH}: {usage:.2f}%")

    if usage > THRESHOLD:
        print("WARNING: Disk usage is above threshold!")
    else:
        print("Disk usage is within safe limits.")

if __name__ == "__main__":
    main()
