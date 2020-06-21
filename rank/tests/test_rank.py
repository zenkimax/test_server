'''
test rank views
'''
# from django.urls import reverse
from rank.tests import TestCase    # pylint: disable=import-error


class RankTestCase(TestCase):
    '''
    测试排名请求
    '''
    def test_ten_client_rank(self):
        '''
        测试请求排名
        '''
