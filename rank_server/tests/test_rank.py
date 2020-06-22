'''
test rank views
'''
from django.urls import reverse
from rank_server.tests import TestCase    # pylint: disable=import-error


class RankTestCase(TestCase):
    '''
    测试排名请求
    '''
    def test_ten_client_rank(self):    # pylint: disable=too-many-locals
        '''
        测试请求排名
        '''
        client_1 = self.login_as('客户端1')
        client_2 = self.login_as('客户端2')
        client_3 = self.login_as('客户端3')
        client_4 = self.login_as('客户端4')
        client_5 = self.login_as('客户端5')
        client_6 = self.login_as('客户端6')
        client_7 = self.login_as('客户端7')
        client_8 = self.login_as('客户端8')
        client_9 = self.login_as('客户端9')
        client_10 = self.login_as('客户端10')

        res_1 = client_1.json_post(reverse('rank_server:add'), data={'username': '1', 'score': 9999999})
        res_2 = client_2.json_post(reverse('rank_server:add'), data={'username': '2', 'score': 9500112})
        res_3 = client_3.json_post(reverse('rank_server:add'), data={'username': '3', 'score': 9233333})
        res_4 = client_4.json_post(reverse('rank_server:add'), data={'username': '4', 'score': 5445444})
        res_5 = client_5.json_post(reverse('rank_server:add'), data={'username': '5', 'score': 3453452})
        res_6 = client_6.json_post(reverse('rank_server:add'), data={'username': '6', 'score': 2342342})
        res_7 = client_7.json_post(reverse('rank_server:add'), data={'username': '7', 'score': 66666})
        res_8 = client_8.json_post(reverse('rank_server:add'), data={'username': '8', 'score': 66666})
        res_9 = client_9.json_post(reverse('rank_server:add'), data={'username': '9', 'score': 76})
        res_10 = client_10.json_post(reverse('rank_server:add'), data={'username': '10', 'score': 75})

        self.assertEqual(res_1.status_code, 200)
        self.assertEqual(res_2.status_code, 200)
        self.assertEqual(res_3.status_code, 200)
        self.assertEqual(res_4.status_code, 200)
        self.assertEqual(res_5.status_code, 200)
        self.assertEqual(res_6.status_code, 200)
        self.assertEqual(res_7.status_code, 200)
        self.assertEqual(res_8.status_code, 200)
        self.assertEqual(res_8.status_code, 200)
        self.assertEqual(res_9.status_code, 200)
        self.assertEqual(res_10.status_code, 200)

        res_rank_list = client_5.get(reverse('rank_server:list'), data={'user': 5, 'start': 0, 'end': 10})
        expect = [[1, "客户端1", 9999999], [2, "客户端2", 9500112], [3, "客户端3", 9233333], [4, "客户端4", 5445444],
                  [5, "客户端5", 3453452], [6, "客户端6", 2342342], [7, "客户端8", 66666], [8, "客户端7", 66666], [9, "客户端9", 76],
                  [10, "客户端10", 75], [5, "客户端5", 3453452]]
        print(res_rank_list.json())
        self.assertEqual(res_rank_list.json(), expect)
