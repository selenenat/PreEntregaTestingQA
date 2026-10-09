import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10) 

    yield driver

    driver.quit()

def test_01_login(driver):
   driver.get("https://www.saucedemo.com/") 

   driver.find_element(By.ID, "user-name").send_keys("standard_user")
   driver.find_element(By.ID, "password").send_keys("secret_sauce")
   driver.find_element(By.ID, "login-button").click()

   assert "/inventory.html" in driver.current_url, "ERROR: No se redirigio a /inventory.html"

def test_02_verificar_inventario( driver ): 
  page_title = driver.title
  section_title = driver.find_element(By.CLASS_NAME, "title").text

  assert page_title == "Swag Labs", f'ERROR: Titulo de ventana esperado "Swag Labs", obtenido {page_title}'

  assert section_title == 'Products', f'ERROR: Titulo de seccion esperado "Products", Obtenido {section_title}'


def test_03_productos_visibles(driver):
    inventory_item = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    # [] len() => ver que tan largo es una lista
    assert len(inventory_item) > 0 , f'ERROR: No se encontraron productos visibles'

def test_04_validad_interfaz( driver ):
    menu_button = driver.find_element(By.ID, 'react-burger-menu-btn')
    filtro = driver.find_element(By.CLASS_NAME,'product_sort_container')

    assert menu_button.is_displayed(), f'ERROR: Menu no esta visible'
    assert filtro.is_displayed(), f'ERROR: filtro no esta visible'

def test_05_añadir_productos_al_carrito(driver):
    # Usar find_elements (en plural) para obtener la lista e indexar [0]
    first_item = driver.find_elements(By.CLASS_NAME, 'inventory_item')[0]
    
    # Hacer clic en el botón 'Add to cart' dentro del primer producto
    add_to_cart_btn = first_item.find_element(By.TAG_NAME, 'button')
    add_to_cart_btn.click()


def test_06_verificar_contador_carrito(driver):
    # Ahora sí existirá la burbuja del carrito con el número "1"
    contador_carrito = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    assert contador_carrito == "1", f'ERROR: Se esperaba 1, obtuvo {contador_carrito}'


def test_07_navegar_carrito(driver):

   driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
   assert "/cart.html" in driver.current_url , "ERROR: No se redirigio a /cart.html"


def test_08_comprobar_poducto_en_el_carrito( driver):
    producto_nombre_en_carrito = driver.find_element(By.CLASS_NAME, 'inventory_item_name').text

    assert producto_nombre_en_carrito == 'Sauce Labs Backpack' , f'ERROR: NO ES EL MISMO NOMBRE'   
