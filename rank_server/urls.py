'''
urls of rank
'''

from django.conf.urls import url, include    # pylint: disable=unused-import
from rank_server import views    # pylint: disable=import-error

urlpatterns = [
    url(r'^add/$', views.RankAPIView.as_view(), name='add'),
    url(r'^list/$', views.RankListAPIView.as_view(), name='list')
]
