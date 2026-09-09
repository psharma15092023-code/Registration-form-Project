from django.urls import path
from . import views 


urlpatterns = [
    path("list/",views.list_registration_items),
    path("insert_registration/",views.insert_registration_item,name="insert_registration_item"),
    path("edit_registration/<int:id>/",views.edit_registration_item,name="edit_registration_item"),
    path("delete/<int:id>/", views.delete_registration_item, name="delete_registration_item"),
]   