import openpyxl
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def executar_etapas_adicionais(driver):
# Carregue a planilha do Excel
    workbook = openpyxl.load_workbook('C:\\Users\\allan.silva\\Desktop\\cursos_filtrados.xlsx')
    sheet = workbook.active

    # Percorra as linhas e compare os valores
    for row in sheet.iter_rows(values_only=True):
        value = row[0]

        if value is None:
            continue

        if value.startswith(('SENAC', 'Comercial', 'PSG')):
            continue

        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input.form-control'))
        )

        # Agora você pode interagir com o elemento
        search_box.send_keys(value)

        # Clique no elemento li
        li_item = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'li.li-item.ng-star-inserted'))
        )
        li_item.click()

        # Aguarde até que o próximo elemento esteja visível e clique nele
        accordion_click = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.col-md-1.accordion-click.seta'))
        )
        accordion_click.click()

        editar_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//i[contains(@class, 'fa-pencil')]/.."))
        )
        driver.execute_script("arguments[0].click();", editar_link)

        # Clique no botão 'Ajustar versão existente'
        ajustar_versao_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'btn-ajustar-versao'))
        )
        ajustar_versao_button.click()


       # Aguarde até que o modal seja visível
        WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'modal-container'))
        )

# Encontre o botão 'Mais opções' dentro do modal
        mais_opcoes_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'modal-container .dropdown-toggle.btn.btn-sm.btn-light.text-primary.btn-white.acoes-listagem'))
        )
        mais_opcoes_button.click()

# Clique no link 'Editar' dentro do modal

# Encontre o elemento através do XPath
        editar_link_modal = driver.find_element(By.XPATH, "//a[contains(text(), 'Editar')]")

# Execute o JavaScript para clicar no elemento
        driver.execute_script("arguments[0].click();", editar_link_modal)

    # Pare aqui, conforme solicitado
        break