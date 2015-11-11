from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
import sys

class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_read_profile(self):
        #toni membuka laman home profile
        self.browser.get(self.server_url+'/activity')

        #toni melihat header dengan tulisan yang mengandung "Profile Faisal"
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("Profile Faisal", header_text)

        #toni melihat subjudul dan menemukan tulisan "Identitas Diri" dan "Kontak & Media Sosial"
        subheader = self.browser.find_elements_by_tag_name('h2')
        self.assertEqual("Identitas Diri",subheader[0].text)
        self.assertEqual("Aktivitas Terdahulu",subheader[1].text)

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
        #toni melihat aktivitas saat ini pada baris kelima tabel
        self.assertIn("Kontak",th[5].text)
        #toni melihat subjudul dan menemukan tulisan "Research" dan "Work"
        subheader = self.browser.find_elements_by_tag_name('h3')
        self.assertEqual("Research",subheader[0].text)
        self.assertEqual("Work",subheader[1].text)

    def test_can_read_home(self):
        #toni membuka laman home profile
        self.browser.get(self.server_url)

        #toni melihat header dengan tulisan yang mengandung "Blog Faisal"
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("Blog Faisal", header_text)

        #toni melihat subjudul dan menemukan tulisan "Lorem Ipsum" dan "Per Enei"
        subheader = self.browser.find_elements_by_tag_name('h2')
        self.assertEqual("Lorem Ipsum Dolor Sit Amet",subheader[0].text)
        self.assertEqual("Per ei veniam lobortis definitiones",subheader[1].text)

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
