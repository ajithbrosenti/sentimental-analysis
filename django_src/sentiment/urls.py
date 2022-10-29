from django.urls import path
from . import views
urlpatterns = [
        path('<str:sentiment>',views.index,name = "sentiment_endpoint"),
]
