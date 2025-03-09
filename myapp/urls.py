

from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list),
    path('Add/', views.add_user),
    path('Edit/<id>', views.EditUser),
    path('Delete/<eid>', views.DeleteUser),
    path('View/<id>', views.ViewUser),
]