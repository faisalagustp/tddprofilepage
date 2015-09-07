from selenium import webdriver

import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_read_home_profile(self):
        self.browser.get('http://localhost:8000')
        self.assertIn("Web Profile Faisal", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("Web Profile Faisal", header_text)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
