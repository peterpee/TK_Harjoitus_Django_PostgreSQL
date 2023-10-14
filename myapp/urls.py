from . import views
from django.urls import path
from .views import SignUpView
from .views import logout_view
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
# from mysite import settings

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('recipe_list/', views.recipe_list, name='recipe_list'),
    path('create/', views.create_recipe, name='create_recipe'),
    path('view/<int:recipe_id>/', views.view_recipe, name='view_recipe'),
    path('logout/', views.logout_view, name='logout_user'),
    path('delete_recipe/<int:recipe_id>/', views.delete_recipe, name='delete'),
]

