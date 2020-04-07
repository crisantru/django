from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView

class HomepageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    # test url
    def test_homepage_status_code(self):
        #response = self.client.get('/')
        self.assertEqual(self.response.status_code, 200)
    
    # test url reverse name
    """def test_homepage_url(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)"""

    # test template of the url
    def test_homepage_template(self):
        #response = self.client.get('/')
        self.assertTemplateUsed(self.response, 'home.html')
    
    # test html of the template
    def test_homepage_contains_correct_html(self):
        #response = self.client.get('/')
        self.assertContains(self.response, 'Homepage')
    
    def test_homepage_does_not_contain_incorrect_html(self):
        #response = self.client.get('/')
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')
    
    # test view
    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )