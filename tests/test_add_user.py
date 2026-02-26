from helpers import open_page, close_page


def test_add_user():
    p, browser, page = open_page()

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.fill("input[name='username']", "Admin")
    page.fill("input[name='password']", "admin123")
    page.click("button[type='submit']")

    page.click("span:has-text('Admin')")
    page.click("button:has-text('Add')")

    page.wait_for_timeout(3000)
    assert page.is_visible("body")

    close_page(p, browser, page)