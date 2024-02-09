from django.urls import path
from .views import registration, log_in, log_out, get_user_info

app_name = 'users'

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('log_in/', log_in, name='log_in'),
    path('log_out/', log_out, name='log_out'),
    path('<int:pk>/', get_user_info, name='get_user_info')
]
