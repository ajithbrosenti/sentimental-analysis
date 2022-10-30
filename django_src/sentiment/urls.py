from django.urls import path
from . import views
urlpatterns = [
        path('',views.index,name = "sentiment_endpoint"),
]
