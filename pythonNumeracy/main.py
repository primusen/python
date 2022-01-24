#   Imports
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
from selenium import webdriver
from pathlib import Path
import time

#   Variables
keyboard = Controller()
dev = '÷'
i = 0

url = 'https://www.drfrostmaths.com/timestables-game.php'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

txt = Path('data.txt').read_text()
em, psw = txt.split()

#   Login
driver.find_element(By.XPATH, '//*[@id="dfm-home-inner-content"]/form/input[1]').click()
keyboard.type(em)
time.sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="dfm-home-inner-content"]/form/input[2]').click()
keyboard.type(psw)
time.sleep(0.5)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(1)
driver.fullscreen_window()
time.sleep(5)

#   Challenge starts
driver.find_element(By.XPATH, '//*[@id="question"]/a').click()
driver.find_element(By.XPATH, '//*[@id="calculator-display"]').click()
time.sleep(0.1)

#   Calculation loop
while i < 70:
    time.sleep(0.35)

    question = driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[1]/div[4]').text

    x, a, y = question.split(" ")

    x = int(x)
    y = int(y)

    if dev in a:
        answer = x // y
    else:
        answer = x * y

    answer = str(answer)
    keyboard.type(answer)

    i += 1
time.sleep(60)
