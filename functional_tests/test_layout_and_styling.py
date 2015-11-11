from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):

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

    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.browser.get(self.server_url+'/todolist')
        self.browser.set_window_size(1024, 500)

        # She notices the input box is nicely centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5
        )

        # She starts a new list and sees the input is nicely
        # centered there too
        inputbox.send_keys('testing\n')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5
        )

    def test_footer_styling(self):
        # Edith goes to the home page
        self.browser.get(self.server_url+'/todolist')
        self.browser.set_window_size(1024, 1000)

        # She lookup the footer and find footer section
        # attached at the bottom
        footer = self.browser.find_element_by_id('footer');
        body =  self.browser.find_element_by_tag_name("body");

        self.assertAlmostEqual(
            footer.location['y'] + footer.size['height'],
            self.browser.get_window_size()['height'] - 79,
            delta=5
        )
