from django.urls import include
from . import views
from rest_framework import routers
from django.conf.urls import url

app_name = 'blog'

router = routers.DefaultRouter()
router.register("blog", views.BlogSearchAPI2, basename="blog-search")
router.register('search2', views.SearchBlogViewSet, basename='search2')

urlpatterns = [
    url(r"v1/", include(router.urls)),
]
