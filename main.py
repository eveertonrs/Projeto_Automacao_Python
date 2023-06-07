import time
import datetime
from playwright.sync_api import sync_playwright

# URL do site
url = 'https://app.linxio.com/login'

# Credenciais de login
username = ''
password = ''

# Inicializar o Playwright
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Abrir uma nova página
    page = context.new_page()

    # Acessar a página de login
    page.goto(url)
    # Preencher as credenciais de login
    # page.locator('xpath=//*[@id="mat-input-93"]').fill(username)
    page.fill("input[formcontrolname='email']", username)
    page.fill("input[formcontrolname='password']", password)

    # Enviar o formulário de login
    page.click('button[type="submit"]')
    time.sleep(3)

    # Aguardar o redirecionamento após o login
    # page.wait_for_navigation()

    # Navegar até o link de relatórios
    page.goto('https://app.linxio.com/client/reports/routes_details/routes')
    time.sleep(5)

    # Calcular a data de ontem
    data_hoje = datetime.date.today()
    data_ontem = data_hoje - datetime.timedelta(days=1)

    # Formatar as datas de ontem no formato desejado
    data_inicial = data_ontem.strftime("%d/%m/%Y") + " 00:00" + " - "
    data_final = data_ontem.strftime("%d/%m/%Y") + " 23:59"

    # Preencher os campos de filtro diretamente
    page.fill("#cdkOverlayTrigger", data_inicial + data_final)
    time.sleep(2)
    # elemento = page.query_selector("[id='cdkOverlayTrigger']")
    # elemento.press("Enter")
    # time.sleep(3)
    # page.click('button[type="submit"]')
    # time.sleep(5)

    page.locator('//*[@id="wrapper"]/div[2]/lin-content/lin-client/div/lin-routes-details/lin-layout-section/div/div[2]/lin-tab-nav-bar/lin-routes/lin-table-settings/button').click()
    time.sleep(2)
    page.locator('//*[@id="wrapper"]/div[2]/lin-content/lin-client/div/lin-routes-details/lin-layout-section/div/div[2]/lin-tab-nav-bar/lin-routes/lin-table-settings/div[2]/div/div[1]/button[1]').click()
    time.sleep(5)

    # Fechar o navegador
    context.close()
