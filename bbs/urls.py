
from django.urls import path
from bbs import views
app_name= 'bbs'
urlpatterns = [
    path('list/',views.b_list,name='b_list'),




]
