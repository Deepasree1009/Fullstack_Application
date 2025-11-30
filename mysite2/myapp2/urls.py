# from django.urls import path
# from .import views

# urlpatterns = [
#         path('', views.home, name='home'),
#     ]


from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.reg, name='register'),
    path('login/', views.login, name='login'),
    path('get/', views.get_all_data, name='get'),
    path('delete/', views.delete_data, name='delete'),
    path('put/', views.update_data, name='put'),
 
   
]



