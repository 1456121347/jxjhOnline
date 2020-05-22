from users import views
from .views import UserProfileViewSet

from django.urls import path

user_list = UserProfileViewSet.as_view({
    'get': 'list'
})


urlpatterns = [
    path('', views.api_root),
    path('users/', user_list, name='user-list')
]