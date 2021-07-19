from django.urls import path
from apps.base.views import index

app_name = "base"
urlpatterns = [
    path('', index, name='home'),
]
