from selenium import webdriver
import time

def abrir_sofascore():
    driver = webdriver.Chrome()
    driver.get("https://www.sofascore.com/pt/torneio/futebol/brazil/brasileirao-serie-a/325#id:72034")
    time.sleep(5)
    return driver