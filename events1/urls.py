from django.urls import path
from events1.views import *
from events1.views import event_det
from django.contrib.auth import views as auth_views

app_name = 'events1'

urlpatterns = [
    path('accounts/login/', login_view, name='login'), 
    path('logout/', logout_view, name='logout'),
    path('accounts/signup/', signup, name='signup'),
    path('', event_list, name='event_list'),
    path('event/<int:pk>/', event_det, name='event_detail'),
    path('event/new/', event_create, name='event_create'),
    path('event/<int:pk>/edit/', event_edit, name='event_edit'),
    path('event/<int:pk>/delete/', event_delete, name='event_delete'),
]