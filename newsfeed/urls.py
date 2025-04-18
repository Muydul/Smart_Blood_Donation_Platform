
from django.urls import path, include
from .views import home, addRequest, seeDetails, arequestAddRemove, seeRequestedDonor, editPost, deletePost, commentPost, deleteComment, contactNow,about

urlpatterns = [



    path('', home, name='home'),
    path('add/', addRequest, name='add-request'),
    path('<pk>/see-details', seeDetails, name='see-details'),
    path('<pk>/edit-post', editPost, name='edit-post'),
    path('<pk>/delete/', deletePost, name='post-delete'),
    path('<pk>/add-req-remove', arequestAddRemove, name='arequest-add-remove'),
    path('<pk>/see-requested-donor', seeRequestedDonor,
         name='see-requested-donor'),

    path('<pk>/comment/', commentPost, name='comment-post'),
    path('<pk>/<ck>/dc/', deleteComment, name='delete-comment'),
    path('<pk>/contact-now/', contactNow, name='contact-now'),
    path('about', about, name='about'),




]
