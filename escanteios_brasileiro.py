import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException

#abre a página
driver = webdriver.Chrome()
driver.get("https://www.sofascore.com/pt/torneio/futebol/brazil/brasileirao-serie-a/325#id:72034")
time.sleep(5)

#dicionário para armazenar os escanteios
escanteios_por_jogo = {}


#obtém o valor da rodada
rodada_element = driver.find_element(By.XPATH, "//div[contains(@class, 'Text') and contains(text(), 'Rodada')]")
rodada_texto = rodada_element.text
rodada = int(rodada_texto.split(" ")[1])


while True:
    #loop para clicar em cada jogo
    boxes = driver.find_elements(By.XPATH, "//div[@class='Box klGMtt sc-efac74ba-1 kugaRD']")
    if len(boxes) > 1:
        for i in range(len(boxes)):
            boxes = driver.find_elements(By.XPATH, "//div[@class='Box klGMtt sc-efac74ba-1 kugaRD']")
            boxes[i].click()
            time.sleep(4)
            
            #faz um try (caso não tenha a estatística encerra o for e volta para a rodada anterior)
            try:
                statistics_tab = driver.find_element(By.XPATH, "//h2[@data-tabid='statistics']/a")
                statistics_tab.click()
                time.sleep(4)

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

            except:
                print(f"Rodada {rodada} ainda não começou ou estatísticas indisponíveis.")
                break  #Sai do for para voltar a rodada

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

driver.quit()

#resultados ordenados
def ordenar_chave(chave):
    partes = chave.split(" ")
    rodada = int(partes[1])
    jogo = int(partes[4])
    return (rodada, jogo)

chaves_ordenadas = sorted(escanteios_por_jogo.keys(), key=ordenar_chave)

for chave in chaves_ordenadas:
    dados = escanteios_por_jogo[chave]
    print(f"{chave} - Mandante: {dados['mandante']}, Visitante: {dados['visitante']}, Total: {dados['total']}")