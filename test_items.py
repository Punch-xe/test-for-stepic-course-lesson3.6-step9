# тест на наличие кнопки Добавить в корзину
import time

def test_submit_button_is_present(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(30)
    add_to_cart = len(browser.find_elements_by_css_selector('.btn.btn-lg.btn-primary'))
    assert add_to_cart > 0, 'no any button "Add to Cart"'

