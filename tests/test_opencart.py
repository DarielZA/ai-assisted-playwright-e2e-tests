from helpers import open_page, close_page

def test_login():
    p, browser, page = open_page()
    
    page = browser.new_page()

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.fill("input[name='username']", "Admin")
    page.fill("input[name='password']", "admin123")

    page.click("button[type='submit']")

    page.wait_for_selector("h6:has-text('Dashboard')")
    assert page.is_visible("h6:has-text('Dashboard')")

    close_page(p, browser, page)