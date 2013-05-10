import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_user_can_login(self):
        # Clive knows of a website which contains lots of torrent that he wants to try out
        # He navigates to it in his browser
        self.browser.get('http://127.0.0.1:8000')

        # He notices that the browser title says he's made it to the right site
        self.assertIn('Forked Tongue', self.browser.title)

        # He is asked to log into the website, He notices this is also in the page title.
        self.assertIn('login', self.browser.title)

        # He types in his login details incorrectly the first time.

        # He notices he is back on the login page, with a message stating his credentials were incorrect.
        # He trys again, and this time successfully logs in.


        # He can tell he's now logged in from the title bar and the user interface displaying his name.
