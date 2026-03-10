from django.urls import path 
from .import views
app_name='app1'
urlpatterns=[
    path('cr/',views.cr,name='cr'),
    path('lr/',views.lr,name='lr'),
    path('fun_t1/',views.fun_t1,name='fun_t1'),
    path('sana/',views.fun_t2,name='sana'),
    path('',views.index,name='index'),


]