from django.urls import path

from . import views

app_name = "Teachers"
urlpatterns = [
    path("", views.index, name="index"),
    
    #Register new teachers urls
    path("newTeacher", views.NewTeacher, name="newTeacher"),
    path("alta", views.Alta, name="alta"),
    
    #Update teachers info urls
    path("<int:teacher_id>/update", views.Update, name="updateInfo"),
    path("<int:teacher_id>/save_update", views.SaveUpdate, name="save_update"),
    
    #Delete teachers urls
    path("<int:teacher_id>/delete", views.Delete, name="delete"),
    
    #Visualize info urls
    path("search",views.Search, name="search"),
    path("<int:teacher_id>/details", views.Details, name="details"),
    
    #test urls
    path("navbar", views.navbar, name="navbar")
]