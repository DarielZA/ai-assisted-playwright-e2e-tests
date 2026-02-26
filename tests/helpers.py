from playwright.sync_api import sync_playwright
import os

def open_page():
    if not os.path.exists("test-results"):
        os.makedirs("test-results")

    p = sync_playwright().start()

    browser = p.chromium.launch(headless=False)

    context = browser.new_context(
        record_video_dir="test-results/",
        record_video_size={"width":1280, "height":720}
    )

    page = context.new_page()
    return p, browser, page


def close_page(p, browser, page):
    page.screenshot(path=f"test-results/{page.url.split('/')[-1] or 'result'}.png")
    browser.close()
    p.stop()