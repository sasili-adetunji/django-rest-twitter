from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from .views import UserTweetView


urlpatterns = [
    url(_(r'^tweet/$'),
        UserTweetView.as_view(),
        name='tweet'),

]
