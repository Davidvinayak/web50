from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>",views.entry,name="entry"),
    path("search/",views.search,name="search"),
    path("new/",views.new,name="newpage"),
    path("edit/<str:ptitle>",views.edit,name="edit"),
    path("save/",views.save_edit,name="save"),
    path("random/",views.random,name="random")

]
