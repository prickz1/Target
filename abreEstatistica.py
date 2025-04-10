import time
from coletaDados import coletar_dados_escanteios
from selenium.webdriver.common.by import By

def acessar_estatisticas_e_coletar(driver, escanteios_por_jogo, rodada, i):
    try:
        statistics_tab = driver.find_element(By.XPATH, "//h2[@data-tabid='statistics']/a")
        statistics_tab.click()
        time.sleep(4)

        #coleta os dados de escanteios
        coletar_dados_escanteios(driver, escanteios_por_jogo, rodada, i)
        return True  #sucesso

    except:
        print(f"Rodada {rodada} ainda não começou ou estatísticas indisponíveis.")
        return False  #falhou, volta pra rodada anterior