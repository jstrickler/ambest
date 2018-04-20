from django.test import TestCase
from django.urls import reverse

TEST_DATA = {
    'Superman': 'Clark Kent',
    'Iron Man': 'Tony Stark',
}

class TestSuperhero(TestCase):
    # use JSON data for mock data
    fixtures = ['superheroes']

    def setUp(self):
        url = reverse("apiv1:superherolist")
        self.superheroes = self.client.get(url).json()
        self.heroes_by_name = {}
        for hero in self.superheroes:
            self.heroes_by_name[hero['name']] = hero

    def test_names(self):
        url = reverse("apiv1:superherodetail", args=(1,))
        response = self.client.get(url)
        self.assertEquals(response.json()['name'], 'Superman', "Content does not contain correct name")

    def test_secret_identities(self):
        for name, secret_identity in TEST_DATA.items():
            self.assertEqual(secret_identity, self.heroes_by_name[name]['secret_identity'], 'secret identities do not match')
