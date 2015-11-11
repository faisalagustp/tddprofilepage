from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):
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
