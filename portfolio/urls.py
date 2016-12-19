from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', portfolio_index),
    url(r'(?P<category_slug>[-\w]*)/$', category_list, name='category_list'),
    url(r'(?P<category_slug>[-\w]*)/(?P<entry_slug>[\w-])$', entry_detail, name='entry_detail')

]
