from django.urls import path
from davomatapp import views

urlpatterns = [
    path('xodimlar/', views.xodim_list, name='xodim_list'),
    path('xodimlar/create/', views.xodim_create, name='xodim_create'),
    path('xodimlar/update/<int:id>/', views.xodim_update, name='xodim_update'),
    path('delete_xodim/<int:id>/', views.xodim_delete, name='delete_ishchi'),
    path('davomat/', views.davomat, name='davomat'),
    path('profile', views.profile, name='profile'),

]
