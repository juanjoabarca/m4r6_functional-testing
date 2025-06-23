from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import tempfile

# Configurar opciones de Chrome
options = Options()
options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")
options.add_argument("--headless")  # Puedes quitar esta línea si quieres ver la ventana
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Iniciar navegador
driver = webdriver.Chrome(options=options)
driver.get("https://duckduckgo.com/")

# Buscar campo de texto
buscador = driver.find_element(By.NAME, "q")
buscador.send_keys("inmuebles en Bogotá")
buscador.send_keys(Keys.RETURN)

# Esperar resultados
time.sleep(2)

# Validar que exista algún resultado
#resultados = driver.find_elements(By.CSS_SELECTOR, ".result")
resultados = driver.find_elements(By.CSS_SELECTOR, 'li[data-layout="organic"]')
assert len(resultados) > 0, "No se encontraron resultados."

print(resultados)

print("✅ Prueba funcional completada con éxito")

driver.quit()