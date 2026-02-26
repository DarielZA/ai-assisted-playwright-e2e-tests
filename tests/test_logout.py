from helpers import open_page, close_page


def test_logout():
    p, browser, page = open_page()
    
    page = browser.new_page()

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.fill("input[name='username']", "Admin")
    page.fill("input[name='password']", "admin123")
    page.click("button[type='submit']")

    page.click("p.oxd-userdropdown-name")
    page.click("a:has-text('Logout')")

    page.wait_for_selector("input[name='username']")
    assert page.is_visible("input[name='username']")

    close_page(p, browser, page)