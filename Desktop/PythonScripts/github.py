import webbrowser

# Specify the URL for GitHub
url = "https://github.com/"

# Register Chrome browser with the correct path
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Update this path if necessary
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

# Open the URL in Chrome
webbrowser.get('chrome').open(url)
