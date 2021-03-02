# тест на наличие кнопки Добавить в корзину
# закоментированы альтернативные способы проверки

import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_submit_button_is_present(browser):
    browser.get(link)
    time.sleep(3)
    assert browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket"), 'no any button "Add to Cart"'
    # add_to_cart = len(browser.find_elements_by_css_selector('.btn.btn-lg.btn-primary'))
    # assert add_to_cart > 0, 'no any button "Add to Cart"'

