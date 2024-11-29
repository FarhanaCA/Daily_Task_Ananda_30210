from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import EventListCreateAPIView, EventRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='event-list'), name='logout'),
    path('', views.event_list, name='event-list'),
    path('create/', views.event_create, name='event-create'),
    path('edit/<int:pk>/', views.event_edit, name='event-edit'),
    path('delete/<int:pk>/', views.event_delete, name='event-delete'),
    path('api/events/', EventListCreateAPIView.as_view(), name='api-event-list-create'),
    path('api/events/<int:pk>/', EventRetrieveUpdateDestroyAPIView.as_view(), name='api-event-detail'),
    
]
