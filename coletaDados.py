import time
from selenium.webdriver.common.by import By

def coletar_dados_escanteios(driver, escanteios_por_jogo, rodada, i):
    corners_elements = driver.find_elements(By.XPATH, "//span[text()='Escanteios']/ancestor::div[@class='Box Flex heNsMA bnpRyo']")
    if corners_elements:
        container = corners_elements[0]
        spans = container.find_elements(By.XPATH, ".//span[@class='Text iZtpCa' or @class='Text lfzhVF']")

        if len(spans) >= 2:
            mandante = spans[0].text
            visitante = spans[1].text
            total = int(mandante) + int(visitante)
            escanteios_por_jogo[f"Rodada {rodada} - Jogo {i+1}"] = {
                "mandante": mandante,
                "visitante": visitante,
                "total": total
            }
            time.sleep(2)
        else:
            print("Não foi possível localizar os valores de escanteios.")
    else:
        print("Elemento de escanteios não encontrado.")
        time.sleep(5)