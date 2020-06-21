'''
urls of rank
'''

from django.conf.urls import url, include    # pylint: disable=unused-import
from rank import views    # pylint: disable=import-error

urlpatterns = [url(r'^(?P<username>)/', views.RankAPIView.as_view(), name='rank_list')]
