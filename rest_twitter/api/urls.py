from django.conf.urls import url, include
from django.utils.translation import ugettext_lazy as _
from rest_framework.routers import DefaultRouter

from .views import UserTweetView, LoginViewSet

router = DefaultRouter()


router.register('login', LoginViewSet, base_name='login')

urlpatterns = [
    url(_(r'^tweet/$'),
        UserTweetView.as_view(),
        name='tweet'),
    url(r'', include(router.urls)),
]
