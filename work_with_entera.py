import time
import keyboard
from data import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:\\Rparobot\\soft\\chromedriver.exe')
driver.maximize_window()
driver.get("https://id.entera.pro/login")


def login_in_entera():
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-input-0"]')))

    lofin_elem = driver.find_element(By.XPATH, '//*[@id="mat-input-0"]')
    lofin_elem.send_keys(general_data['Entera login'])

    pass_elem = driver.find_element(By.XPATH, '//*[@id="mat-input-1"]')
    pass_elem.send_keys(general_data['Entera pas'])
    pass_elem.send_keys(Keys.ENTER)


def load_file_in_entera():
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, entera_logo_xpath)))
    driver.find_element(By.CLASS_NAME, entera_logo_xpath).click() # todo слишком долго ищет, надо как то решить

    driver.find_element(By.XPATH, '//*[@id="mat-dialog-0"]/ng-component/div/entera-file-upload-zone/div/div[1]/span')\
        .click() # todo цикл для нескольких файлов сделать
    time.sleep(3)
    keyboard.write(general_data['path_to_files'])
    keyboard.send("enter")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="mat-dialog-0"]/ng-component/div/div/button/span').click()