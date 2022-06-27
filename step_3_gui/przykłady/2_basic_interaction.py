from collections import namedtuple
from dataclasses import dataclass
from time import sleep

from faker import Faker
from selene import config, browser
from selene.conditions import visible, attribute
from selene.support.conditions import have, be
from selene.support.conditions.have import size_greater_than_or_equal
from selene.support.jquery_style_selectors import s, ss


class User:
    def __init__(self, username, password, email):
        self.email = email
        self.password = password
        self.username = username

@dataclass
class User:
    username: str
    password: str
    email: str

class Header:
    def __init__(self):
        self.sign_in_button = s("[ggloginbutton]")
        self.join_button = s("gg-menu-nav-nouser a[href='/join']")

    def open_sign_in_modal(self):
        self.sign_in_button.click()

    def go_to_user_registration(self):
        self.join_button.click()


class SignInModal:
    def __init__(self):
        self.username_field = s("#inputUsername")
        self.password_field = s("#inputPassword")
        # self.sign_in_button = s("//button[normalize-space()='Sign In']")

    def login(self, user: User):
        sleep(2)
        self.username_field.type(user.username)
        self.password_field.type(user.password).press_enter()
        # self.sign_in_button.click()


class RegistrationForm:
    def __init__(self):
        self.username_field = s("#join-username")
        self.email_field = s("#join-email")
        self.password_field = s("#join-password")
        self.create_account_button = s("[type='submit']")
        self.skip_button = s("//*[normalize-space()='Skip']")

    def fill_user_data(self, user: User):
        self.username_field.type(user.username)
        self.email_field.type(user.email)
        self.password_field.type(user.password)
        self.create_account_button.click()
        self.skip_button.click()

Game = namedtuple("Game", ["title", "ownership"])
def add_game(game: Game):
    s("a [alt='Add a Game']").click()
    s("input[name='geekitemname']").type(game.title)
    ss(".searchbox_results_title + *") \
        .should_have(size_greater_than_or_equal(1))
    ss(".searchbox_results_title + *").first().click()
    own_checkbox = s("#addowned")
    if attribute(own_checkbox, "checked") and game.ownership == "No":
        own_checkbox.click()
    elif not attribute(own_checkbox, "checked") and game.ownership == "Yes":
        own_checkbox.click()
    s("#addgame input[type='button']").click()
    s(".searchbox_results_title").should_not_be(visible)





username = "<some_username>"
password = "<some_username>"
fake = Faker()
env = f"http://boardgamegeek.com/"
config.timeout = 10
config.start_maximized = True
# my_user = User(fake.first_name() + fake.first_name()+ fake.first_name(), fake.password(length=10), fake.email())
my_user = User(username, password, "")
header = Header()
sign_in_modal = SignInModal()
# registration_form = RegistrationForm()
# # początek procesu
browser.open_url(env)
# header.open_sign_in_modal()
# sign_in_modal.login(user_name=username, user_password=password)
sleep(1)
s('#c-p-bn').click()
# header.go_to_user_registration()
# registration_form.fill_user_data(my_user)
#
header.open_sign_in_modal()
sign_in_modal.login(my_user)

s(".mygeek-dropdown-username").click()
sleep(1)
s("//a[@class='dropdown-item' and text()='Collection']").click()
sleep(1)
add_game(Game("Talisman", "No"))
sleep(10)
