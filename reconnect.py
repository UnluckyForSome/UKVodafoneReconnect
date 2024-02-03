import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_script_directory():
    # Get the directory where the script is located
    return os.path.dirname(os.path.abspath(__file__))

def routerconfig(query, passwd):
    browser = webdriver.Chrome()
    browser.get(query)

    WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login-txt-pwd"]')))
    search = browser.find_elements(By.ID, "login-txt-pwd")[0]
    search.click()
    search.send_keys(passwd)
    time.sleep(1)

    WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login-btn-logIn"]')))
    searchBtn = browser.find_elements(By.ID, "login-btn-logIn")[0]
    searchBtn.click()
    time.sleep(1)

    WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, '// *[ @ id = "StatusSupport"]')))
    searchConfig = browser.find_elements(By.XPATH, '// *[ @ id = "StatusSupport"]')[0]
    searchConfig.click()
    time.sleep(1)

    WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, '// *[ @ id = "restart"]')))
    searchRebot = browser.find_elements(By.XPATH, '// *[ @ id = "restart"]')[0]
    searchRebot.click()
    time.sleep(1)

    WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, '// *[ @ id = "restart-btn-reconnect_dsl"]')))
    searchReconnect = browser.find_elements(By.XPATH, '// *[ @ id = "restart-btn-reconnect_dsl"]')[0]
    searchReconnect.click()
    time.sleep(1)

    WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, '// *[ @ id = "restart-dsl-btn-apply"]')))
    searchReconnect = browser.find_elements(By.XPATH, '// *[ @ id = "restart-dsl-btn-apply"]')[0]
    #searchReconnect.click()

    time.sleep(30)  # Important sleep to allow reconnect to send properly

    browser.quit()

print("@author Joseph McClemont")
print("@license http://www.gnu.org/licenses/gpl.html")

# Password Handler
try:
    # Construct the path to configRouter.txt relative to the script directory
    config_file_path = os.path.join(get_script_directory(), "configRouter.txt")

    with open(config_file_path, "r") as f:
        data = f.readlines()

    #  format list of config vars
    configRouter = [line.rstrip('\n') for line in open(config_file_path)]
    configRouter = [w.replace('password=', '') for w in configRouter]

    try:  # check if file is empty
        password = configRouter[0]
    except:
        pass

    f.close()

except IOError:
    # Construct the path to configRouter.txt relative to the script directory
    config_file_path = os.path.join(get_script_directory(), "configRouter.txt")

    file = open(config_file_path, 'w', newline='\n')
    print("\nRouter connector config\n")

    #  user input for new password
    password = input("Password: ")
    file.write("password=" + password)

    file.close()

routerconfig("http://192.168.1.1/", password)