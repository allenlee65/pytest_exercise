import random
import string
import time
import os

def generate_random_email():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"test_{random_string}@example.com"

def generate_random_name():
    names = ["John", "Jane", "Mike", "Sarah", "David", "Emma", "Alex", "Lisa"]
    return random.choice(names) + str(random.randint(100, 999))

def wait_for_file_download(download_dir: str, extension: str = '.txt', timeout: int = 30):
    """Wait for a file with specified extension to appear in download_dir"""
    elapsed = 0
    while elapsed < timeout:
        files = os.listdir(download_dir)
        for f in files:
            if f.endswith(extension):
                return os.path.join(download_dir, f)
        time.sleep(1)
        elapsed += 1
    raise TimeoutError(f"No file with extension {extension} downloaded in {download_dir} within {timeout} seconds")
