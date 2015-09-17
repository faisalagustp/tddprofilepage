from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from profileapp.models import Item
from profileapp.views import *

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_root_url_resolves_to_activity_view(self):
        found = resolve('/activity/')
        self.assertEqual(found.func, activity_page)

    def test_activity_page_returns_correct_html(self):
        request = HttpRequest()
        response = activity_page(request)
        expected_html = render_to_string('activity.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_root_url_resolves_to_todolist_page_view(self):
        found = resolve('/todolist/')
        self.assertEqual(found.func, todolist_page)

    def test_todolist_page_returns_correct_html(self):
        request = HttpRequest()
        response = todolist_page(request)
        expected_html = render_to_string('todolist.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_todolist_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = todolist_page(request)

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_todolist_page_redirect_after_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = todolist_page(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/todolist/the-only-list-in-the-world/')

    def test_todolist_page_only_saves_items_when_necessary(self):
        request = HttpRequest()
        todolist_page(request)
        self.assertEqual(Item.objects.count(), 0)

    def todolist_page_show_comments(self, number, message):
        for x in range(0, number):
            Item.objects.create(text='itemey '+str(number))
        request = HttpRequest()
        response = view_list(request)

        self.assertIn(message, response.content.decode())

    def test_todolist_page_shows_comments_no_item(self):
        self.todolist_page_show_comments(0, "yey, waktunya berlibur")
        self.todolist_page_show_comments(4, "sibuk tapi santai")
        self.todolist_page_show_comments(5, "oh tidak")

class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')

class ListViewTest(TestCase):

    def test_uses_list_template(self):
        response = self.client.get('/todolist/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_all_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/todolist/the-only-list-in-the-world/') #1

        self.assertContains(response, 'itemey 1') #2
        self.assertContains(response, 'itemey 2') #3
