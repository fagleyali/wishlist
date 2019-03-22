from django.urls import path
from . import views

urlpatterns=[
    path('',views.WishList.as_view(),name='wish_list'),
    path('add/',views.WishCreate.as_view(),name='wishes_create'),
    path('delete/<int:wish_id>',views.wish_delete,name='wishes_delete')

]