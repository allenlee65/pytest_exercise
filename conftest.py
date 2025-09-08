import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from dotenv import load_dotenv


@pytest.fixture(scope='function')
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--headless")  # Comment out to see browser UI
    chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values": {"geolocation": 2}})
    chrome_options.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

@pytest.fixture(scope='session')
def base_url():
    return "http://automationexercise.com"

@pytest.fixture(scope='session')
def credentials():
    email = os.getenv('AE_TEST_EMAIL')
    password = os.getenv('AE_TEST_PASSWORD')
    if not email or not password:
        raise ValueError("Environment variables AE_TEST_EMAIL and AE_TEST_PASSWORD must be set for tests.")
    return {"email": email, "password": password}

# 根目錄下的 Conftest.py

# 在 Jenkins 中 Secret File 的 Variable 命為 ENV_FILE
# 當環境變數含有 ENV_FILE 代表正在 Jenkins 上運行，應用 load_dotenv () 讀取 Secret File
# 若沒有 ENV_FILE，則會讀取本地的 .env 檔
if 'ENV_FILE' in os.environ:
    env_file = os.environ['ENV_FILE']
    load_dotenv(env_file)

# 這寫法可讓你在本地端 ／ Jenkins 都能正常運作而不用修改程式碼。