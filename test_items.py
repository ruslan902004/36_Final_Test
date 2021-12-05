#import time

from typing import Text


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_btn_add_to_basket(browser):
    browser.get(link)
    #time.sleep(60)
    assert browser.find_element_by_css_selector('[class="btn btn-lg btn-primary btn-add-to-basket"]'), 'Dont find button add to basket'
    
    