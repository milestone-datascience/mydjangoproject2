from django.urls import path
from .views import post,post_page

urlpatterns = [
  path("",post),
  path("<int:id>",post_page)
]