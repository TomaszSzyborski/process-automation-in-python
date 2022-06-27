from time import sleep

from selene import config, browser
from selene.conditions import visible, clickable
from selene.support.jquery_style_selectors import s
from faker import Faker

env = f"http://boardgamegeek.com/"
config.timeout = 5
config.start_maximized = True

faker = Faker()

user_name = faker.name().replace(' ', '')
email = faker.ascii_email()
password = faker.password(length=10)

browser.open_url(env)


s('a[routerlink="/join"]').click()
s('#join-username').type(user_name)
s('#join-email').type(email)
s('#join-password').type(password)
s('button[type="submit"]').click()
#s('button[type="button"]').click()
#s('//*[text()=" Skip "]')
sleep(5)