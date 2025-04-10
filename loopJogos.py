import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
from abreEstatistica import acessar_estatisticas_e_coletar

def loop_jogos(driver, escanteios_por_jogo, rodada_inicial):
    rodada = rodada_inicial

    while True:
        boxes = driver.find_elements(By.XPATH, "//div[@class='Box klGMtt sc-efac74ba-1 kugaRD']")
        if len(boxes) > 1:
            for i in range(len(boxes)):
                boxes = driver.find_elements(By.XPATH, "//div[@class='Box klGMtt sc-efac74ba-1 kugaRD']")
                boxes[i].click()
                time.sleep(4)

                sucesso = acessar_estatisticas_e_coletar(driver, escanteios_por_jogo, rodada, i)
                if not sucesso:
                    break  #Sai do for para voltar à rodada anterior

        else:
            print("Próximo jogo não encontrado.")
            break

        #tenta voltar para a rodada anterior com segurança
        try:
            wait = WebDriverWait(driver, 10)
            button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='Button iCnTrv']")))
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
            time.sleep(1)
            driver.execute_script("arguments[0].click();", button)
            time.sleep(5)
            rodada -= 1
        except (TimeoutException, ElementNotInteractableException):
            print("Não foi possível voltar para a rodada anterior.")
            break

    return rodada