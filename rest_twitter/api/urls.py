from django.conf.urls import url, include
from django.utils.translation import ugettext_lazy as _
from rest_framework.routers import DefaultRouter

from .views import UserTweetView, LoginViewSet, UserProfileViewSet

router = DefaultRouter()


router.register('profile', UserProfileViewSet)
router.register('login', LoginViewSet, base_name='login')  # needs basename coz its not model viewsets


urlpatterns = [
    url(_(r'^tweet/$'),
        UserTweetView.as_view(),
        name='tweet'),
    url(r'', include(router.urls)),
]
