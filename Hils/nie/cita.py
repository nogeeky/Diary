import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

lets_go = True

while lets_go == True:
    browser = webdriver.Chrome()
    browser.get("https://sede.administracionespublicas.gob.es/icpplus/index.html")

    city = browser.find_element(By.XPATH, '//*[@id="form"]/option[34]')
    city.click()

    page1button = browser.find_element(By.XPATH, "//input[@id='btnAceptar']")
    page1button.click()

    page2_form = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="tramiteGrupo[0]"]/option[17]')))

    page2_form.click()

    page2_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='btnAceptar']")))

    page2_button.click()

    page3_enter = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='btnEntrar']")))

    time.sleep(3)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    page3_enter.click()

    niebox = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="txtIdCitado"]')))

    niebox.click()
    niebox.send_keys("YOUR NIE")

    name_box = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='txtDesCitado']")))

    time.sleep(2)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    niebox.click()
    name_box.send_keys("YOUR NAME")

    page4_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='btnEnviar']")))

    page4_button.click()

    time.sleep(2)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    cita_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="btnEnviar"]')))

    cita_button.click()

    no_appointments = browser.page_source.find("En este momento no hay citas disponibles.") 

    if no_appointments:
        browser.close()
        time.sleep(2100)
    else:
        os.system("say 'Hey, Appointments are available'")
        time.sleep(2)
        os.system("say 'Hey, Appointments are available'")
        time.sleep(2)
        os.system("say 'Hey, Appointments are available'")
        time.sleep(2)
        os.system("say 'Hey, Appointments are available'")
        lets_go = False
        break