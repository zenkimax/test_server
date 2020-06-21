'''
rank views
'''
# import json
import redis
from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.exceptions import (NotFound)
# Create your views here.


class RankAPIView(APIView):
    '''
    更新、查询排名
    '''
    def __init__(self):
        super().__init__()
        self.pool = redis.ConnectionPool(host='172.16.153.134', port=6379)

    def post(self, request):
        '''
        更新排名数据
        '''
        score = request.data.get('score')
        username = request.data.get('username')
        redis_conn = redis.Redis(connection_pool=self.pool)
        redis_conn.zadd('rank', username, score)
