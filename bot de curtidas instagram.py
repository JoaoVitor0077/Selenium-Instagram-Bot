from pyparsing import conditionAsParseAction
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as CondicaoExperada
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300,1000', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ]
    )
    return driver, wait


driver, wait = iniciar_driver()
# Entrar no site do instagram
driver.get('https://www.instagram.com/')
sleep(5)
# Clicar e digitar meu email
campo_email = wait.until(CondicaoExperada.element_to_be_clickable(
    (By.XPATH, "//input[@name='username']")))
campo_email.send_keys('')
sleep(5)
# Clicar e digitar minha senha
campo_senha = wait.until(CondicaoExperada.element_to_be_clickable(
    (By.XPATH, "//input[@name='password']")))
campo_senha.send_keys('')
sleep(5)
# Clicar no campo entrar
entrar = wait.until(CondicaoExperada.element_to_be_clickable(
    (By.XPATH, "//div[text()='Entrar']")))
entrar.click()
sleep(5)
# Navegar até a página alvo
while True:
    # Colocar o link da página alvo qui
    driver.get('')
    sleep(10)
    # Clicar na última  postagem
    postagens = wait.until(CondicaoExperada.visibility_of_any_elements_located(
        (By.XPATH, "//div[@class='_aagu']")))
    sleep(10)
    postagens[0].click()
    sleep(10)
    # Verificar se postagem foi curtida, caso não tenha sido, clicar curtir, caso já tenha sido, aguardar 24hrs
    elementos_postagem = wait.until(
        CondicaoExperada.visibility_of_any_elements_located((By.XPATH, "_abm0 _abl_")))
    if len(elementos_postagem) == 6:
        elementos_postagem[0].click()
        sleep(86400)
    else:
        print('Postagem já curtida')
        sleep(86400)
input('')
driver.close()
