from django.test import TestCase
from mixer.backend.django import mixer


class BaseSetup(TestCase):
    def setUp(self):
        # mixer adds 6 to the argument specified in the cycle function
        self.users = mixer.cycle(3).blend('authentication.User')
        self.diaries = mixer.cycle(3).blend('diary.Diary')
        self.entries = mixer.cycle(3).blend('entry.Entry')
