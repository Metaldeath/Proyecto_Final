from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.PageListView.as_view(), name='list'),
    path('create/', views.PageCreateView.as_view(), name='create'),
    path('<int:pk>/', views.PageDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.PageUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.PageDeleteView.as_view(), name='delete'),
]
