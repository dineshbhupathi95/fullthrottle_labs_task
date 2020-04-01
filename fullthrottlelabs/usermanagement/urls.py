from django.conf.urls import url
from . import views
urlpatterns = [
    url('users', views.UserListView.as_view())
]