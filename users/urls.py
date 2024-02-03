from django.urls import path
from .views import registration

app_name = 'users'

urlpatterns = [
    path('', registration, name='registration')
]
