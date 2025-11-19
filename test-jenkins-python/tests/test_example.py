def test_google_title(browser):
    browser.get("https://www.google.com")
    assert "Google" in browser.title

def test_fail_example(browser):
    browser.get("https://www.google.com")
    assert "Bing" in browser.title  # This will fail
