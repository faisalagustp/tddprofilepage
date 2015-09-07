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
        self.assertIn("Profile Faisal", header_text)
        subheader_text = self.browser.find_elements_by_tag_name('h2')
        self.assertEqual("Identitas Diri",subheader_text[0].text)
        self.assertEqual("Kontak & Media Sosial",subheader_text[1].text)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
