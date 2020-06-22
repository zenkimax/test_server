'''
rank views
'''
import redis
from rest_framework.views import APIView
from rest_framework.response import Response


class RankAPIView(APIView):
    '''
    更新排名
    '''
    def __init__(self):
        super().__init__()
        self.pool = redis.ConnectionPool(host='127.0.0.1', port=6379)

    def post(self, request):
        '''
        更新排名数据
        '''
        score = int(request.data.get('score'))
        username = request.data.get('username')
        redis_conn = redis.Redis(connection_pool=self.pool)
        res = redis_conn.zadd('rank', {username: score})
        return Response('add success %s' % (res + 1))


class RankListAPIView(APIView):
    '''
    查询排名
    '''
    def __init__(self):
        super().__init__()
        self.pool = redis.ConnectionPool(host='127.0.0.1', port=6379)

    def get(self, request):
        '''
        更新排名数据
        '''
        username = request.query_params.get('user')
        offset = int(request.query_params.get('offset'))
        redis_conn = redis.Redis(connection_pool=self.pool)
        score = redis_conn.zscore('rank', username)
        user_rank = redis_conn.zrank('rank', username)

        z_rev_range = redis_conn.zrevrangebyscore('rank',
                                                  max=10000000,
                                                  min=0,
                                                  start=offset,
                                                  num=10,
                                                  withscores=True,
                                                  score_cast_func=int)
        result = []
        for i in range(10):
            result.append([offset + 1 + i, '客户端%s' % (z_rev_range[i][0].decode('utf-8')), z_rev_range[i][1]])
        result.append([user_rank, '客户端%s' % username, int(score)])

        return Response(result)
