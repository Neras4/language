
def test_different_languages(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    a = None
    browser.get(link)
    a = browser.find_element_by_css_selector('button.btn-primary')
    assert a is not None 
