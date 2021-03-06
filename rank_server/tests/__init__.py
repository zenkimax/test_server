'''
init TestCase
'''
import datetime
import pytz
from django.test import TestCase as django_TestCase
from django.conf import settings
from django.urls import reverse

from common.django.drf.client import APIClient    # pylint:disable=import-error


class TestCase(django_TestCase):
    '''
    base TestCase
    '''
    client = None
    now = datetime.datetime(2020, 1, 1, tzinfo=pytz.timezone('UTC'))
    now_str = '2020-01-01T08:00:00+08:00'
    mock_now = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def gen_client(username):
        '''
        gen client by token
        '''
        client = APIClient()
        client.head = {'user': username}
        return client

    def login_as(self, username):
        '''
        gen test client from user
        '''
        return self.gen_client(username)

    def setUp(self):
        '''
        pre-work
        '''
        self.init()

    def tearDown(self):
        pass

    def init(self):
        '''
        something else to init
        '''
