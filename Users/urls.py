from django.urls import path
from .views import AllUsers

app_name = 'Users'

urlpatterns = [
    path('', AllUsers),
]