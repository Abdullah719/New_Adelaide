from django.conf.urls import url
from first_app import views

app_name = 'first_app'

urlpatterns = [

    url(r'^help',views.help ,name='help'),
    url(r'^form', views.forms_view, name='forms_view'),
    url(r'^user_login', views.user_login, name='user_login')

]