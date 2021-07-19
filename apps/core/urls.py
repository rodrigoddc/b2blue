from django.urls import path
from apps.core.views import show_list, show_detail, show_discover, show_vote

app_name = "core"
urlpatterns = [
    path('top-100/', show_list, name='top-100'),
    path('details/<int:pk>', show_detail, name='show-detail'),
    path('discover/', show_discover, name='show-discover'),
    path('vote/<int:pk>', show_vote, name='show-vote'),
]
