from selenium.webdriver.common.by import By

def obter_rodada(driver):
    rodada_element = driver.find_element(By.XPATH, "//div[contains(@class, 'Text') and contains(text(), 'Rodada')]")
    rodada_texto = rodada_element.text
    rodada = int(rodada_texto.split(" ")[1])
    return rodada