from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
    """
    def test_can_read_home_profile(self):
        #toni membuka laman home profile
        self.browser.get('http://localhost:8000')

        #toni mengecek title browser dan menunjukkan "Web Profile Faisal"
        self.assertIn("Web Profile Faisal", self.browser.title)

        #toni melihat header dengan tulisan yang mengandung "Profile Faisal"
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("Profile Faisal", header_text)

        #toni melihat subjudul dan menemukan tulisan "Identitas Diri" dan "Kontak & Media Sosial"
        subheader = self.browser.find_elements_by_tag_name('h2')
        self.assertEqual("Identitas Diri",subheader[0].text)
        self.assertEqual("Kontak & Media Sosial",subheader[1].text)

        #toni juga menemukan link dengan nama Activity
        activity_link = self.browser.find_element_by_partial_link_text('Activity')
        self.assertTrue(activity_link)
        #Link tersebut mengarah ke /activity
        self.assertIn("/activity",activity_link.get_attribute("href"))

        th = self.browser.find_elements_by_tag_name("th");
        #toni melihat nama pemilik web pada baris pertama tabel
        self.assertIn("Nama",th[0].text)
        #toni melihat tempat tanggal lahir pemilik web pada baris kedua tabel
        self.assertIn("Tempat Tanggal Lahir",th[1].text)
        #toni melihat alamat pemilik web pada baris ketiga tabel
        self.assertIn("Alamat",th[2].text)
        #toni melihat pendidikan terakhir pemilik web pada baris keempat tabel
        self.assertIn("Pendidikan Terakhir",th[3].text)
        #toni melihat aktivitas saat ini pada baris kelima tabel
        self.assertIn("Aktivitas Saat Ini",th[4].text)


    def test_can_read_activity_page(self):
        #toni membuka laman activity
        self.browser.get('http://localhost:8000/activity')

        #toni mengecek title browser dan menunjukkan "Web Profile Faisal"
        self.assertIn("Web Profile Faisal", self.browser.title)

        #toni melihat header dengan tulisan yang mengandung "Aktivitas Faisal"
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("Aktivitas Faisal", header_text)

        #toni melihat subjudul dan menemukan tulisan "Research" dan "Work"
        subheader = self.browser.find_elements_by_tag_name('h2')
        self.assertEqual("Research",subheader[0].text)
        self.assertEqual("Work",subheader[1].text)

        #toni juga menemukan link dengan nama Activity
        home_link = self.browser.find_element_by_partial_link_text('Home')
        self.assertTrue(home_link)
    """
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # toni membuka bagian todolist dalam website tersebut
        self.browser.get(self.live_server_url+'/todolist')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        #page showing that the "komentar" on that page is: yey, waktunya berlibur
        komentar = self.browser.find_element_by_id('komentar').text
        self.assertTrue(komentar)
