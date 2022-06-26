from time import sleep

from selene import config, browser

env = f"http://boardgamegeek.com/"
config.timeout = 20
config.start_maximized = True

browser.open_url(env)
sleep(10)
