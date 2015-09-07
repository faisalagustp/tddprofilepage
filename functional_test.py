from selenium import webdriver

import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

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
        self.browser.get('http://localhost:8000/activity')
        self.assertIn("Web Profile Faisal", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("Aktivitas Faisal", header_text)
        subheader = self.browser.find_elements_by_tag_name('h2')
        self.assertEqual("Research",subheader[0].text)
        self.assertEqual("Work",subheader[1].text)
        activity_link = self.browser.find_element_by_partial_link_text('Home')
        self.assertTrue(activity_link)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
