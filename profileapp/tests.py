from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

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
        self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string(
            'todolist.html',
            {'new_item_text':  'A new list item'}
        )
        self.assertEqual(response.content.decode(), expected_html)
