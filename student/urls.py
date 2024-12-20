from django.urls import path,include
from . import views

urlpatterns =[
    path("index/",views.index,name="index"),
    path("<int:id>",views.view_student,name="view_student"),
    path("add/",views.add,name="add"),
    path("edit/<int:id>/",views.edit,name="edit"),
    path("delete/<int:id>/",views.delete,name="delete"),
    path("",views.login_view,name="login"),
    path("registration/",views.register_view,name="registration")


    #path("accounts/",include("django.contrib.auth.urls")),
]