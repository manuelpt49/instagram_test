#Django
from django.urls import path
from django.views.generic import TemplateView

#Views
from users import views

urlpatterns = [
    #Posts


    #Management
    path(
        route='login/',
        view=views.login_view,
        name='login'),
    path(
        route='logout/',
        view=views.logout_view,
        name='logout'),
    path(
        route='signup/',
        view=views.signup,
        name='signup'),
    path(
        route='me/profile/',
        view=views.update_profile,
        name='update_profile'),
]

