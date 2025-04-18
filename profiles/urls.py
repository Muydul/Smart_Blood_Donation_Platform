from django.urls import path, include
from .views import myProfile,editMyProfile,getProfile


urlpatterns = [


    path('my-profile/', myProfile, name='my-profile'),
    path('edit-profile/<pk>/edit/', editMyProfile, name='edit-profile'),
    path('<pk>/get-profile/', getProfile, name='get-profile'),




]
