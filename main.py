from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

timeout = 30 # por exemplo

driver_path = r'C:\Users\allan.silva\Desktop\webscraping\msedgedriver.exe'

# Defina as opções
edge_options = Options()
edge_options.use_chromium = True

# Crie um objeto de serviço
service = Service(driver_path)

# Crie o driver
driver = webdriver.Edge(service=service, options=edge_options)

# URL da página de login
url = 'https://cloud.plataforma.senac.br/#/login?returnUrl=%2F'

# Navegue até a página de login
driver.get(url)

wait = WebDriverWait(driver, 10)  # Espera por até 10 segundos


# Selecione "DR-MT" na lista suspensa
print("Selecionando 'DR-MT' na lista suspensa...")
select_regional = Select(wait.until(EC.presence_of_element_located((By.ID, 'regional'))))
select_regional.select_by_value('DR-MT')

# Marque a caixa de seleção
print("Marcando a caixa de seleção...")
checkbox = wait.until(EC.element_to_be_clickable((By.ID, 'salvar-regional')))
checkbox.click()

# Clique no botão "Continuar"
print("Clicando no botão 'Continuar'...")
botao_continuar = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn-primary.btn-block')))
botao_continuar.click()

# Encontre os campos de e-mail e senha usando os IDs fornecidos
print("Inserindo e-mail e senha...")
campo_email = wait.until(EC.presence_of_element_located((By.ID, 'email')))
campo_email.send_keys('xxxxxxxxxxxxxx')
campo_senha = driver.find_element(By.ID, 'senha')
campo_senha.send_keys('xxxxxxxxxxxx')

# Código anterior ...

# Clique no botão de login
botao_login = driver.find_element(By.CLASS_NAME, 'btn-primary')
botao_login.click()

# Aguarde a presença de um elemento específico que indica que o login foi bem-sucedido
element_present = EC.presence_of_element_located((By.CLASS_NAME, 'small-box-footer'))
WebDriverWait(driver, timeout).until(element_present)

# Navegue até a página desejada após a autenticação
from selenium.webdriver.common.by import By

# URL desejada após a autenticação
url_acao_educacional = 'https://cloud.plataforma.senac.br/planocurso/#/acao-educacional'
driver.get(url_acao_educacional)
print("Redirecionado para a página de ação educacional")

# Aguarda o carregamento do script específico
script_src = "main.eb741988deee1480d72c.js"
script_loaded = False

for _ in range(timeout * 10): # Tentará encontrar o elemento 10 vezes por segundo por 10 segundos
    scripts = driver.find_elements(By.CSS_SELECTOR, f'script[src="{script_src}"]')
    if scripts:
        script_loaded = True
        print("Script carregado!")
        break
    time.sleep(0.1)

if not script_loaded:
    print("Script não carregado no tempo esperado")
    
from etapas_adicionais import executar_etapas_adicionais

executar_etapas_adicionais(driver)

input("Pressione Enter para fechar o navegador...")



