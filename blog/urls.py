from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.BlogSearchAPI.as_view(), name='search'),
]
