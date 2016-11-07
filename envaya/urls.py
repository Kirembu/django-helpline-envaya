from django.conf.urls import url, include
from envaya import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^admin/', views.admin),
]
