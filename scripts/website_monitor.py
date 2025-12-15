import requests
import logging

logging.basicConfig(filename='../logs/automation.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# List of websites to monitor
WEBSITES = [
    "https://www.google.com",
    "https://www.github.com",
    # Add client sites here
]

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"[OK] {url} is UP (Status: {response.status_code})")
            logging.info(f"Website {url} is UP.")
        else:
            print(f"[WARNING] {url} returned status {response.status_code}")
            logging.warning(f"Website {url} returned status {response.status_code}")
    except requests.ConnectionError:
        print(f"[DOWN] {url} is unreachable.")
        logging.error(f"Website {url} is unreachable.")
    except requests.Timeout:
        print(f"[TIMEOUT] {url} timed out.")
        logging.error(f"Website {url} timed out.")

def main():
    print("--- Website Monitor ---")
    for site in WEBSITES:
        check_website(site)

if __name__ == "__main__":
    main()