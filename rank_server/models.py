'''
sqlite3 models
'''
import os
from django.db import models
# from common.django.model import BaseModel
from common.django.model import BaseModel    # pylint: disable=import-error

BASEDIR = os.path.dirname(os.path.abspath(__file__))


class Rank(BaseModel):
    '''
    排名表
    '''
    username = models.CharField(max_length=255, blank=False, verbose_name='用户名')
    rank = models.IntegerField(default=10000000, verbose_name='排名')
    score = models.IntegerField(default=0, verbose_name='分数')
